from apps.core.permissions import IsCompany, IsSuperUser, IsReferrer
from apps.core.viewsets import CreateListRetrieveViewSet
from apps.referral.models import Referral


class ReferralViewSet(CreateListRetrieveViewSet):
    permission_class_mapper = {
        'create': [IsReferrer],
        'list': [IsReferrer | IsCompany | IsSuperUser],
        'retrieve': [IsReferrer | IsCompany | IsSuperUser]
    }

    queryset = Referral.objects.all()

