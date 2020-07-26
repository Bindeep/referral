from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.referrer.models import Referrer
from apps.users.api.v1.serializers import UserDetailSerializer


class ReferrerSerializer(DynamicFieldsModelSerializer):
    user = UserDetailSerializer()

    class Meta:
        model = Referrer
        fields = '__all__'
