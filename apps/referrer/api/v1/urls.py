from rest_framework import routers

from apps.referrer.api.v1.views import ReferrerViewSet

app_name = 'referrer'

router = routers.DefaultRouter()


router.register(
    r'',
    ReferrerViewSet,
    basename='referrer'
)


urlpatterns = [
]

urlpatterns += router.urls
