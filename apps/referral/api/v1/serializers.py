from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.referral.models import Referral


class ReferralSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Referral
        fields = '__all__'
