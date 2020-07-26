from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.referral.models import Referral
from apps.referrer.api.v1.serializers import ReferrerSerializer


class ReferralSerializer(DynamicFieldsModelSerializer):
    referrer = ReferrerSerializer()

    class Meta:
        model = Referral
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        if self.request and self.request.method == 'GET':
            fields['referrer'] = ReferrerSerializer()
            fields['company'] = CompanySerializer()
        return fields

