from rest_framework import serializers

from apps.common.api.v1.serializers import CitySerializer
from apps.company.models import Company, Category, Product, CompanyCategory
from apps.core.mixins.serializers import DynamicFieldsModelSerializer


class CategorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CompanyCategorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CompanyCategory
        fields = '__all__'

    def create(self, validated_data):
        if self.context.get('company'):
            validated_data['company'] = self.context.get('company')
        return super().create(validated_data)


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


class ProductSerializer(DynamicFieldsModelSerializer):
    commission = serializers.FloatField(min_value=0, max_value=100)

    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        if self.context.get('company'):
            validated_data['company'] = self.context.get('company')
        return super().create(validated_data)

    def update_get_fields(self, fields):
        fields['category'] = serializers.ReadOnlyField(source='category.name')
        return fields
