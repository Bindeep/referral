from rest_framework.decorators import action

from apps.core.permissions import IsCompany, IsSuperUser, IsReferrer
from apps.core.viewsets import CreateListRetrieveViewSet, CreateListRetrieveUpdateViewSet
from apps.referral.api.v1.serializers import ReferralSerializer
from apps.referral.models import Referral


class ReferralViewSet(CreateListRetrieveUpdateViewSet):
    permission_class_mapper = {
        'create': [IsReferrer],
        'list': [IsReferrer | IsCompany | IsSuperUser],
        'retrieve': [IsReferrer | IsCompany | IsSuperUser],
        'update': [IsCompany | IsSuperUser],
    }

    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.user.is_company:
            qs = qs.filter(self.user.company)
        elif self.user.is_referrer:
            qs = qs.filter(self.user.referrer)
        return qs

    @action(
        detail=True,
        methods=['post', ],
        serializer_class=ReferralSerializer,
        url_name='update_amount',
        url_path='amount-update',
        serializer_include_fields=['amount']
    )
    def update_amount(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    @action(
        detail=True,
        methods=['post', ],
        serializer_class=ReferralSerializer,
        url_name='update_status',
        url_path='status-update',
        serializer_include_fields=['status']
    )
    def update_status(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)
