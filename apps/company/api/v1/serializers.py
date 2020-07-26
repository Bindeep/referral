from rest_framework import serializers

from apps.company.models import Company, Category
from apps.core.mixins.serializers import DynamicFieldsModelSerializer


class CategorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CompanySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

    def update_get_fields(self, fields):
        fields['category'] = serializers.ReadOnlyField(source='category.name')
        fields['city'] = serializers.ReadOnlyField(source='city.name')
        fields['contact_person'] = serializers.ReadOnlyField(source='user.full_name')
        return fields
