from rest_framework import serializers

from apps.common.models import City, Article, UserNotification
from apps.core.fields import Base64ImageField
from apps.core.mixins.serializers import DynamicFieldsModelSerializer


class CitySerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class ArticleSerializer(DynamicFieldsModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Article
        fields = '__all__'

    def update_get_fields(self, fields):
        fields['image'] = serializers.ImageField(use_url=True, read_only=True)
        return fields


class UserNotificationSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = UserNotification
        fields = '__all__'
