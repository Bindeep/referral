from rest_framework import routers

from apps.referral.api.v1.views import ReferralViewSet, ReferralLogViewSet

app_name = 'referral'

router = routers.DefaultRouter()


router.register(
    r'log',
    ReferralLogViewSet,
    basename='log'
)

router.register(
    r'',
    ReferralViewSet,
    basename='referral'
)


urlpatterns = [
]

urlpatterns += router.urls
