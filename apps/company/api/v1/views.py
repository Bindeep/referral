from apps.company.api.v1.serializers import CategorySerializer, CompanySerializer
from apps.company.models import Category, Company
from apps.core.permissions import IsSuperUser
from apps.core.viewsets import CreateListUpdateViewSet, ListViewSet


class CompanyViewSet(ListViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSuperUser]
    serializer_include_fields = [
        'referral_code', 'city',
        'name', 'contact_person',
        'description',
        'location',
        'category'
    ]


class CategoryViewSet(CreateListUpdateViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUser]

    def get_serializer_exclude_fields(self):
        if self.request.method.upper() == 'POST':
            return ['slug']
        return super().get_serializer_exclude_fields()
