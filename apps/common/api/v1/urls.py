from rest_framework import routers

from apps.common.api.v1 import views
from apps.common.api.v1.views import NotificationViewSet

app_name = 'common'

router = routers.DefaultRouter()

router.register(
    r'city',
    views.CityViewSet,
    basename='city'
)


router.register(
    r'article',
    views.ArticleViewSet,
    basename='article'
)

router.register(
    r'notification/(?P<user_id>(\d+|me))',
    NotificationViewSet,
    basename='notification'
)

urlpatterns = [
]

urlpatterns += router.urls
