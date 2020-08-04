from django.db.models import Sum
from rest_framework import serializers

from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.referral.constants import COMPLETED
from apps.referrer.models import Referrer
from apps.users.api.v1.serializers import UserDetailSerializer


class ReferrerSerializer(DynamicFieldsModelSerializer):
    user = UserDetailSerializer(fields=[
        'full_name', 'email', 'gender',
        'phone', 'profile_picture'
    ])

    referred = serializers.ReadOnlyField(source='referred_by.name', allow_null=True)
    earned = serializers.SerializerMethodField()

    class Meta:
        model = Referrer
        fields = '__all__'

    @staticmethod
    def get_earned(referrer):
        return referrer.referrals.filter(
            status=COMPLETED
        ).aggregate(total=Sum('commission_amount')).get('total')
