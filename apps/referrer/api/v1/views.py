from apps.core.permissions import IsSuperUser, IsReferrer
from apps.core.viewsets import ListRetrieveUpdateViewSet
from apps.referrer.api.v1.mixins.profile import ReferrerProfileViewSetMixin
from apps.referrer.api.v1.serializers import ReferrerSerializer
from apps.referrer.models import Referrer


class ReferrerViewSet(ReferrerProfileViewSetMixin, ListRetrieveUpdateViewSet):
    queryset = Referrer.objects.all()
    serializer_class = ReferrerSerializer
    permission_classes = [IsSuperUser | IsReferrer]

    def get_object(self):
        return self.referrer
