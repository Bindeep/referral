from apps.company.api.v1.serializers import CategorySerializer
from apps.company.models import Category
from apps.core.viewsets import CustomModelViewSet


class CategoryViewSetViewSet(CustomModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


