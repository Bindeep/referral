from django.urls import path
from rest_framework import routers

from apps.common.api.v1.views import DashboardAPIView
from apps.company.api.v1.views import CategoryViewSet, CompanyViewSet, ProductViewSet, CompanyCategoryViewSet

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

router.register(
    r'company-category',
    CompanyCategoryViewSet,
    basename='company-category'
)

router.register(
    r'product',
    ProductViewSet,
    basename='product'
)

urlpatterns = [
    path('dashboard', DashboardAPIView.as_view(), name='dashboard')
]

urlpatterns += router.urls
