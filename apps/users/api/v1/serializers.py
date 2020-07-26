from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.validators import FileExtensionValidator
from django.db import transaction
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, PasswordField

from apps.common.models import City
from apps.company.models import Category, Company
from apps.core.mixins.serializers import DummySerializer, DynamicFieldsModelSerializer
from apps.core.validators import validate_attachment
from apps.referrer.models import Referrer

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

    class Meta:
        model = USER
        read_only_fields = ('created_at', 'last_login', 'id')
        fields = (
            'id',
            'full_name',
            'email',
            'gender',
            'phone_number',
            'created_at',
            'is_staff',
            'last_login',
            'profile_picture',
        )
        extra_kwargs = {
            'full_name': {
                'required': True,
                'allow_blank': False
            },
            'gender': {
                'required': False,
                'allow_blank': True
            },
            'profile_picture': {
                'required': False,
                'allow_null': True,
                'validators': [
                    FileExtensionValidator(
                        allowed_extensions=['jpg', 'png']
                    ),
                    validate_attachment
                ],
                'use_url': True
            },
            'email': {
                'validators': [
                    UniqueValidator(
                        queryset=USER.objects.all(),
                        lookup='iexact',
                        message=_("You cannot create account with this email address.")
                    )
                ]
            },
            'phone_number': {
                'validators': []
            }
        }

    def get_fields(self):
        fields = super().get_fields()
        if self.request and self.request.method.upper() == 'POST':
            fields['password1'] = PasswordField(max_length=20, min_length=5)
            fields['password2'] = PasswordField(max_length=20, min_length=5)
            fields['referral_code'] = serializers.CharField(
                max_length=10,
                allow_null=True,
                required=False,
                allow_blank=True
            )
        return fields

    def validate(self, attrs):
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 and password2 and password1 != password2:
            raise serializers.ValidationError(_(
                'Both Password must be same'
            ))

        phone_number = attrs.get('phone_number')

        user_qs = USER.objects.all()

        if self.instance:
            user_qs = user_qs.exclude(id=self.instance.id)

        if user_qs.filter(phone_number=phone_number).exists():
            raise serializers.ValidationError({
                'phone_number': _(
                    'You cannot create user with this phone number.'
                )
            })
        return super().validate(attrs)


class AdminRegisterSerializer(DynamicFieldsModelSerializer):
    password = PasswordField(max_length=15, min_length=5)
    repeat_password = PasswordField(max_length=15, min_length=5)

    class Meta:
        model = USER
        fields = [
            'email', 'full_name', 'phone', 'gender',
            'profile_picture', 'password', 'repeat_password'
        ]

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
                company=company
            )
        return user


class CompanyRegisterSerializer(AdminRegisterSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False)
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
    )
    city = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
    )
    location = serializers.CharField(max_length=255)

    class Meta(AdminRegisterSerializer.Meta):
        model = USER
        fields = AdminRegisterSerializer.Meta.fields + [
            'name', 'description', 'category',
            'city', 'location'
        ]

    def create(self, validated_data):
        name = validated_data.pop('name', None)
        description = validated_data.pop('description', None)
        category = validated_data.pop('category', None)
        city = validated_data.pop('city', None)
        location = validated_data.pop('location', None)

        with transaction.atomic():
            user = super().create(validated_data)
            company = Company(
                user=user,
                name=name,
                description=description,
                category=category,
                city=city,
                location=location
            )
            company.save()
        return user


class CustomTokenObtainPairSerializer(DummySerializer, TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = UserDetailSerializer(instance=self.user).data
        return data
