from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.common.api.v1.serializers import (
    CitySerializer, ArticleSerializer
)
from apps.common.models import City, Article
from apps.core.permissions import IsSuperUser
from apps.core.viewsets import ReadOnlyViewSet, CustomModelViewSet, CreateListUpdateViewSet


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
