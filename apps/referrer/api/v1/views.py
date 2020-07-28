from django.db.models import Count, Q
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.permissions import IsSuperUser, IsReferrer
from apps.core.viewsets import ListRetrieveUpdateViewSet
from apps.referral.constants import PENDING, PROGRESS, FAILED, COMPLETED
from apps.referral.models import Referral
from apps.referrer.api.v1.mixins.profile import ReferrerProfileViewSetMixin
from apps.referrer.api.v1.serializers import ReferrerSerializer
from apps.referrer.models import Referrer


class ReferrerViewSet(ReferrerProfileViewSetMixin, ListRetrieveUpdateViewSet):
    queryset = Referrer.objects.all()
    serializer_class = ReferrerSerializer
    permission_classes = [IsSuperUser | IsReferrer]
    serializer_include_fields = ['user', 'referred', 'dob']

    def get_object(self):
        return self.referrer

    @action(detail=True, url_path='stats', url_name='stats')
    def stats(self, request, *args, **kwargs):
        stats = Referral.objects.filter(referrer=self.referrer).aggregate(
            total=Count('id'),
            pending=Count('id', filter=Q(status=PENDING)),
            progress=Count('id', filter=Q(status=PROGRESS)),
            failed=Count('id', filter=Q(status=FAILED)),
            converted=Count('id', filter=Q(status=COMPLETED))
        )
        return Response(stats)
