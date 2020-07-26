from rest_framework import routers

from apps.referrer.api.v1.views import ReferrerViewSet

app_name = 'referral'

router = routers.DefaultRouter()


router.register(
    r'',
    ReferrerViewSet,
    basename='referral'
)


urlpatterns = [
]

urlpatterns += router.urls
