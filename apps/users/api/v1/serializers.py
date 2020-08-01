import copy

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, PasswordField

from apps.common.models import City
from apps.company.models import Category, Company
from apps.core.mixins.serializers import DummySerializer, DynamicFieldsModelSerializer, DummyObject
from apps.referrer.models import Referrer
from apps.users.models import UserDevice

USER = get_user_model()


class PasswordChangeSerializer(DummySerializer):
    password1 = PasswordField(max_length=20, min_length=5)
    password2 = PasswordField(max_length=20, min_length=5)

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 != password2:
            raise serializers.ValidationError(_(
                'Both Password must be same'
            ))
        return super().validate(attrs)


class UserDetailSerializer(DynamicFieldsModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = USER
        read_only_fields = ('created_at', 'last_login', 'id')
        fields = (
            'id',
            'full_name',
            'email',
            'gender',
            'phone',
            'is_staff',
            'last_login',
            'profile_picture',
            'user_type'
        )

    @staticmethod
    def get_user_type(user):
        if user.is_company:
            return 'Company'
        if user.is_referrer:
            return 'Referrer'
        else:
            return 'Admin'


class AdminRegisterSerializer(DynamicFieldsModelSerializer):
    password = PasswordField(max_length=30, min_length=5)
    repeat_password = PasswordField(max_length=30, min_length=5)

    class Meta:
        model = USER
        fields = [
            'email', 'full_name', 'phone', 'gender',
            'profile_picture', 'password', 'repeat_password'
        ]
        extra_kwargs = {
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=USER.objects.all(),
                        lookup='iexact',
                        message=_("You cannot create account with this email address.")
                    )
                ]
            },
            'phone': {
                'validators': [
                    UniqueValidator(
                        queryset=USER.objects.all(),
                        message=_("You cannot create account with this phone number.")
                    )
                ]
            }
        }

    @staticmethod
    def validate_password(password):
        """validate password using django's password validator"""
        validate_password(password)
        return password

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.get('repeat_password')
        if password1 != password2:
            raise serializers.ValidationError('Both Password must be same')
        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('repeat_password')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class ReferrerRegisterSerializer(AdminRegisterSerializer):
    dob = serializers.DateField(required=False, allow_null=True, write_only=True)
    company = serializers.SlugRelatedField(
        queryset=Company.objects.all(),
        slug_field='referral_code',
        allow_null=True,
        required=False
    )

    class Meta(AdminRegisterSerializer.Meta):
        model = USER
        fields = AdminRegisterSerializer.Meta.fields + ['dob', 'company']

    def create(self, validated_data):
        dob = validated_data.pop('dob', None)
        company = validated_data.pop('company', None)

        with transaction.atomic():
            user = super().create(validated_data)
            Referrer.objects.create(
                user=user,
                dob=dob,
                referred_by=company
            )
        return user


class CompanyRegisterSerializer(AdminRegisterSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    city = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
    )
    location = serializers.CharField(max_length=255)

    class Meta(AdminRegisterSerializer.Meta):
        model = USER
        fields = AdminRegisterSerializer.Meta.fields + [
            'name', 'description',
            'city', 'location'
        ]

    def create(self, validated_data):
        copied_data = copy.deepcopy(validated_data)
        name = validated_data.pop('name', None)
        description = validated_data.pop('description', None)
        city = validated_data.pop('city', None)
        location = validated_data.pop('location', None)

        with transaction.atomic():
            user = super().create(validated_data)
            company = Company(
                user=user,
                name=name,
                description=description,
                location=location
            )
            if city:
                company.cities.add(city)
            company.save()
        return DummyObject(**copied_data)


class CustomTokenObtainPairSerializer(DummySerializer, TokenObtainPairSerializer):

    def validate(self, attrs):
        print(attrs)
        data = super().validate(attrs)
        data['user'] = UserDetailSerializer(instance=self.user).data
        return data


class UserDeviceSerializer(DynamicFieldsModelSerializer):

    def create(self, validated_data):
        if self.request and self.request.user:
            validated_data['user'] = self.request.user
        return super().create(validated_data)

    class Meta:
        model = UserDevice
        exclude = ['is_active', 'created_at', 'user']
        extra_kwargs = {
            "registration_id": {
                "validators": []
            }
        }
