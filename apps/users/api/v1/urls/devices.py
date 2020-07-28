from rest_framework import routers

from apps.users.api.v1.views import (
    UserDeviceViewSet)

app_name = 'devices'

router = routers.DefaultRouter()
router.register(r'', UserDeviceViewSet, basename='device')


urlpatterns = [

]

urlpatterns += router.urls
