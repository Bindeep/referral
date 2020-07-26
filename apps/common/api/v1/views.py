from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.common.api.v1.serializers import (
    CountrySerializer, ProvinceSerializer,
    CitySerializer, DistrictSerializer, ArticleSerializer
)
from apps.common.models import (
    Country, Province, City,
    District, Article
)
from apps.core.permissions import IsSuperUser
from apps.core.viewsets import ReadOnlyViewSet, CustomModelViewSet


class CommonViewSet(ReadOnlyViewSet):
    permission_classes = []
    serializer_include_fields = ['name', 'id']
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['name', ]


class CountryViewSet(CommonViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class ProvinceViewSet(CommonViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer
    filter_fields = ['country', ]


class DistrictViewSet(CommonViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filter_fields = ['province', ]


class CityViewSet(CommonViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_fields = ['district', ]


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
