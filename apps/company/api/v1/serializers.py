from rest_framework import serializers

from apps.common.api.v1.serializers import CitySerializer
from apps.company.models import Company, Category, Product, CompanyCategory, ProductImage
from apps.core.mixins.fields import Base64ImageField
from apps.core.mixins.serializers import DynamicFieldsModelSerializer


class CategorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'company': {
                'required': False
            }
        }

    def create(self, validated_data):
        if self.context.get('company'):
            validated_data['company'] = self.context.get('company')
        return super().create(validated_data)


class CompanyCategorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CompanyCategory
        fields = '__all__'


class CompanySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

    def update_get_fields(self, fields):
        fields['cities'] = CitySerializer(
            fields=['name', 'id'],
            many=True
        )
        fields['contact_person'] = serializers.ReadOnlyField(source='user.full_name')
        fields['phone_number'] = serializers.ReadOnlyField(source='user.phone')
        fields['email'] = serializers.ReadOnlyField(source='user.email')
        fields['category'] = serializers.ReadOnlyField(source='category.name')
        return fields


class ProductImageSerializer(DynamicFieldsModelSerializer):

    class Meta:
        pass
        model = ProductImage
        fields = '__all__'
        extra_kwargs = {
            'image': {
                'use_url': True
            }
        }


class ProductSerializer(DynamicFieldsModelSerializer):
    commission = serializers.FloatField(min_value=0, max_value=100)
    images = serializers.ListField(child=Base64ImageField(), write_only=True)

    class Meta:
        model = Product
        fields = '__all__'
        extra_kwargs = {
            'company': {
                'required': False
            }
        }

    def get_fields(self):
        fields = super().get_fields()
        view = self.context.get('view')
        if view and view.action.lower() in ['create', 'update']:
            fields['images'] = serializers.ListField(
                child=Base64ImageField(), write_only=True)
        else:
            fields['images'] = ProductImageSerializer(
                many=True, fields=['image'],
                read_only=True,
                context=self.context
            )
        return fields

    def create(self, validated_data):
        if self.context.get('company'):
            validated_data['company'] = self.context.get('company')

        images = validated_data.pop('images', [])
        instance = super().create(validated_data)

        if images:
            self.add_images(instance, images)
        return instance

    def update(self, instance, validated_data):
        images = validated_data.pop('images', [])
        instance = super().update(instance, validated_data)

        if images:
            self.add_images(instance, images)
        return instance

    def update_get_fields(self, fields):
        fields['category'] = serializers.ReadOnlyField(source='category.name')
        return fields

    @staticmethod
    def add_images(instance, images):
        product_images = [
            ProductImage(image=image, product=instance) for image in images
        ]
        ProductImage.objects.bulk_create(product_images)
