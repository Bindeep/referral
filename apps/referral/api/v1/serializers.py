from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.referral.models import Referral, ReferralLog


class ReferralLogSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ReferralLog
        fields = '__all__'


class ReferralSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Referral
        exclude = ['referrer']

    def create(self, validated_data):
        validated_data['referrer'] = self.context.get('referrer')
        return super().create(validated_data)
