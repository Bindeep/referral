from apps.common.api.v1.serializers import CitySerializer
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
        fields['category'] = CategorySerializer(fields=['id', 'name'])
        fields['city'] = CitySerializer(fields=['id', 'name'])
        return fields
