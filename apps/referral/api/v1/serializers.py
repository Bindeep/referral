from rest_framework import serializers

from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.referral.constants import COMPLETED
from apps.referral.models import Referral, ReferralLog


class ReferralLogSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ReferralLog
        fields = '__all__'


class ReferralSerializer(DynamicFieldsModelSerializer):
    commission_amount = serializers.ReadOnlyField()

    class Meta:
        model = Referral
        exclude = ['referrer']

    def create(self, validated_data):
        validated_data['referrer'] = self.context.get('referrer')
        return super().create(validated_data)

    def validate(self, attrs):
        if self.instance and self.instance.status == COMPLETED:
            raise serializers.ValidationError('Referral cannot be changed once converted')
        return super().validate(attrs)
