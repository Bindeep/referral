from apps.company.api.v1.serializers import CategorySerializer
from apps.company.models import Category
from apps.core.permissions import IsSuperUser
from apps.core.viewsets import CreateListUpdateViewSet


class CategoryViewSet(CreateListUpdateViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]

    def get_serializer_exclude_fields(self):
        if self.request.method.upper() == 'POST':
            return ['slug']
        return super().get_serializer_exclude_fields()
