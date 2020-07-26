from apps.company.api.v1.serializers import CategorySerializer
from apps.company.models import Category
from apps.core.permissions import IsSuperUser
from apps.core.viewsets import CreateListUpdateViewSet


class CategoryViewSet(CreateListUpdateViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]
