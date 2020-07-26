from rest_framework import routers
from apps.common.api.v1 import views


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

urlpatterns = [
]

urlpatterns += router.urls
