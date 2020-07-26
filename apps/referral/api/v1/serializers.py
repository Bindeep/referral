from rest_framework import serializers

from apps.company.api.v1.serializers import CompanySerializer
from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.referral.models import Referral
from apps.referrer.api.v1.serializers import ReferrerSerializer


class ReferralSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Referral
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        if self.request and self.request.method == 'GET':
            fields['referrer'] = ReferrerSerializer()
            fields['company'] = CompanySerializer()
        return fields

    def update_get_fields(self, fields):
        new_fields = ['full_name', 'phone', 'email']
        for field in new_fields:
            fields[field] = serializers.ReadOnlyField(source='referrer.user.{}'.format(field))
        return super().update_get_fields(fields)
