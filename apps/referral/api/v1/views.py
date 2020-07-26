from apps.core.permissions import IsCompany, IsSuperUser, IsReferrer
from apps.core.viewsets import CreateListRetrieveViewSet
from apps.referral.api.v1.serializers import ReferralSerializer
from apps.referral.models import Referral


class ReferralViewSet(CreateListRetrieveViewSet):
    permission_class_mapper = {
        'create': [IsReferrer],
        'list': [IsReferrer | IsCompany | IsSuperUser],
        'retrieve': [IsReferrer | IsCompany | IsSuperUser]
    }

    queryset = Referral.objects.all()
    serializer_class = ReferralSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.user.is_company:
            pass
        return super().get_queryset()
