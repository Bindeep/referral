from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.api.v1.serializers import (
    CitySerializer, ArticleSerializer
)
from apps.common.models import City, Article
from apps.core.permissions import IsSuperUser, IsCompany
from apps.core.viewsets import ReadOnlyViewSet, CustomModelViewSet, CreateListUpdateViewSet
from apps.referral.constants import PENDING, PROGRESS, FAILED, COMPLETED
from apps.referral.models import Referral
from apps.referrer.models import Referrer


class DashboardAPIView(APIView):
    permission_classes = [IsSuperUser | IsCompany]

    def get(self, request, *args, **kwargs):
        referral_qs = Referral.objects.all()
        referrers_qs = Referrer.objects.all()
        referral_code = ''

        user = request.user
        if user.is_company:
            referral_qs = referral_qs.filter(company__user=user)
            referrers_qs = referral_qs.filter(company=user.company)
            referral_code = user.company.referral_code

        company = self.request.query_params.get('company')
        if company:
            referral_qs = referral_qs.filter(company_id=company)

        referral_info = referral_qs.aggregate(
            total=Count('id'),
            pending=Count('id', filter=Q(status=PENDING)),
            progress=Count('id', filter=Q(status=PROGRESS)),
            failed=Count('id', filter=Q(status=FAILED)),
            converted=Count('id', filter=Q(status=COMPLETED))
        )

        referral_info['referrers'] = referrers_qs.count()
        referral_info['referral_code'] = referral_code

        return Response(referral_info)


class CommonViewSet(ReadOnlyViewSet):
    permission_classes = []
    serializer_include_fields = ['name', 'id']
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['name', ]


class CityViewSet(CreateListUpdateViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    search_fields = ['name', ]
    permission_class_mapper = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsSuperUser],
        'update': [IsSuperUser]
    }


class ArticleViewSet(CustomModelViewSet):
    queryset = Article.objects.filter(is_archived=False)
    serializer_class = ArticleSerializer
    permission_class_mapper = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsSuperUser],
        'update': [IsSuperUser],
        'destroy': [IsSuperUser],
    }

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_archived = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
