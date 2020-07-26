from apps.common.models import Country, Province, District, City, Article
from apps.core.mixins.serializers import DynamicFieldsModelSerializer


class CountrySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Country
        fields = '__all__'


class ProvinceSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Province
        fields = '__all__'


class DistrictSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = District
        fields = '__all__'


class CitySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class ArticleSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
