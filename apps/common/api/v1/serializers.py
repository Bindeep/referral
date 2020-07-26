from apps.common.models import City, Article
from apps.core.mixins.serializers import DynamicFieldsModelSerializer


class CitySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class ArticleSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
