from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path('user/', include('apps.users.api.v1.urls.users')),
    path('referrer/', include('apps.referrer.api.v1.urls')),
    path('referral/', include('apps.referral.api.v1.urls')),
    path('common/', include('apps.common.api.v1.urls')),
    path('company/', include('apps.company.api.v1.urls'))
]
