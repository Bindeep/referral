from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.core.permissions import IsSuperUser
from apps.core.viewsets import CreateListRetrieveViewSet, ReadOnlyViewSet
from apps.users.api.v1.serializers import (
    UserDetailSerializer,
    CustomTokenObtainPairSerializer, PasswordChangeSerializer,
    ReferrerRegisterSerializer, AdminRegisterSerializer, CompanyRegisterSerializer
)

USER = get_user_model()


class CustomTokenViewBase(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserViewSet(ReadOnlyViewSet):
    serializer_class = UserDetailSerializer
    queryset = USER.objects.filter(is_active=True)
    permission_class_mapper = {
        'referrer_register': [AllowAny],
        'company_register': [IsSuperUser],
        'admin_register': [IsSuperUser],
        'list': [IsSuperUser],
        'retrieve': [IsSuperUser]
    }
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = ['full_name', 'email', 'phone_number']

    @action(
        detail=False,
        methods=['post', ],
        serializer_class=ReferrerRegisterSerializer,
        url_name='register_referrer',
        url_path='referrer-register'
    )
    def referrer_register(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    @action(
        detail=False,
        methods=['post', ],
        serializer_class=CompanyRegisterSerializer,
        url_name='register_company',
        url_path='register-company'
    )
    def company_register(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    @action(
        detail=False,
        methods=['post', ],
        serializer_class=AdminRegisterSerializer,
        url_path='register_admin',
        url_name='admin-register',
    )
    def admin_register(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
