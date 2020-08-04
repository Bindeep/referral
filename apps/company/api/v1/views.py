from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from apps.company.api.v1.serializers import CategorySerializer, CompanySerializer, ProductSerializer, \
    CompanyCategorySerializer, ProductImageSerializer
from apps.company.models import Category, Company, Product, CompanyCategory, ProductImage
from apps.core.mixins.serializers import DynamicFieldsModelSerializer
from apps.core.permissions import IsSuperUser, IsReadOnly, IsCompany
from apps.core.utils.filter import FilterMapBackend
from apps.core.viewsets import CreateListUpdateViewSet, ListViewSet, CustomModelViewSet, DestroyViewSet


class CompanyViewSet(ListViewSet):
    queryset = Company.objects.select_related('user').prefetch_related('cities')
    serializer_class = CompanySerializer
    permission_classes = [IsSuperUser]
    serializer_include_fields = [
        'referral_code', 'cities',
        'name', 'contact_person',
        'description', 'phone_number',
        'location', 'email'
    ]


class CategoryViewSet(CreateListUpdateViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_class_mapper = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsSuperUser | IsCompany],
        'update': [IsSuperUser | IsCompany]
    }
    filter_backends = (FilterMapBackend, )

    filter_map = {
        'company__category': 'company__category',
    }

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['company'] = self.company
        return ctx

    @property
    def company(self):
        if self.request.user.is_company:
            return self.request.user.company
        else:
            return None

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_company:
            qs = qs.filter(company=self.request.user.company).distinct()
        return qs

    def get_serializer_exclude_fields(self):
        if self.request.method.upper() == 'POST':
            return ['slug']
        return super().get_serializer_exclude_fields()


class CompanyCategoryViewSet(CreateListUpdateViewSet):
    queryset = CompanyCategory.objects.all()
    serializer_class = CompanyCategorySerializer
    permission_class_mapper = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsSuperUser],
        'update': [IsSuperUser]
    }

    def get_serializer_exclude_fields(self):
        if self.request.method.upper() == 'POST':
            return ['slug']
        return super().get_serializer_exclude_fields()


class ProductViewSet(CustomModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_class_mapper = {
        'list': [IsAuthenticated],
        'retrieve': [IsAuthenticated],
        'create': [IsSuperUser | IsCompany],
        'update': [IsSuperUser | IsCompany],
        'destroy': [IsSuperUser | IsCompany],
    }

    filter_backends = (DjangoFilterBackend, )

    filter_fields = {
        'company__category': ['exact'],
        'category': ['exact'],
        'company__cities': ['exact'],
    }

    def get_queryset(self):
        qs = super().get_queryset()
        if self.company:
            qs = qs.filter(company=self.company)
        return qs

    def get_serializer_exclude_fields(self):
        if self.request.method.upper() == 'POST':
            return ['slug']
        return super().get_serializer_exclude_fields()

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['company'] = self.company
        return ctx

    @property
    def company(self):
        if self.request.user.is_company:
            return self.request.user.company
        else:
            return None


class ProductImageViewSet(DestroyViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [IsSuperUser | IsCompany]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.company:
            qs = qs.filter(product__company=self.company)
        return qs

    @property
    def company(self):
        if self.request.user.is_company:
            return self.request.user.company
        else:
            return None
