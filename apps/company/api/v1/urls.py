from rest_framework import routers

app_name = 'company'

router = routers.DefaultRouter()

router.register(
    r'country',
    views.CountryViewSet,
    basename='country'
)

router.register(
    r'district',
    views.DistrictViewSet,
    basename='district'
)

router.register(
    r'city',
    views.CityViewSet,
    basename='city'
)

router.register(
    r'province',
    views.ProvinceViewSet,
    basename='province'
)

urlpatterns = [
]

urlpatterns += router.urls
