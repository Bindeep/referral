from rest_framework import routers

from apps.company.api.v1.views import CategoryViewSet, CompanyViewSet

app_name = 'company'

router = routers.DefaultRouter()

router.register(
    r'',
    CompanyViewSet,
    basename='company'
)

router.register(
    r'category',
    CategoryViewSet,
    basename='category'
)

urlpatterns = [
]

urlpatterns += router.urls
