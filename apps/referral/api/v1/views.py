from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.common.constants import POSITIVE, NEGATIVE, INFO
from apps.common.models import UserNotification
from apps.core.permissions import IsCompany, IsSuperUser, IsReferrer
from apps.core.viewsets import CreateListRetrieveUpdateViewSet, CreateListViewSet
from apps.referral.api.v1.serializers import ReferralSerializer, ReferralLogSerializer
from apps.referral.constants import FAILED, COMPLETED
from apps.referral.models import Referral, ReferralLog


class ReferralViewSet(CreateListRetrieveUpdateViewSet):
    permission_class_mapper = {
        'create': [IsReferrer],
        'list': [IsReferrer | IsCompany | IsSuperUser],
        'retrieve': [IsReferrer | IsCompany | IsSuperUser],
        'update': [IsCompany | IsSuperUser],
    }
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['status']

    queryset = Referral.objects.select_related('city', 'referrer', 'company', 'product')
    serializer_class = ReferralSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        if self.action == 'create':
            ctx['referrer'] = self.request.user.referrer
        return ctx

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        if self.action == 'update':
            return self.http_method_not_allowed(request)

    def get_serializer_exclude_fields(self):
        if self.action == 'create':
            return ['status']
        return super().get_serializer_exclude_fields()

    def get_queryset(self):
        qs = super().get_queryset()
        if self.user.is_company:
            qs = qs.filter(company=self.user.company)
        elif self.user.is_referrer:
            qs = qs.filter(referrer=self.user.referrer)
        return qs

    @action(
        detail=True,
        methods=['put', ],
        serializer_class=ReferralSerializer,
        url_name='update_status',
        url_path='status-update',
        serializer_include_fields=['status']
    )
    def update_status(self, request, *args, **kwargs):
        obj = self.get_object()
        current_status = obj.status
        status = request.data.get('status')

        serializer = self.update_referral(request, *args, **kwargs)

        if current_status != status:
            self.add_status_notification(
                obj,
                current_status,
                status
            )
        return Response(serializer.data)

    @action(
        detail=True,
        methods=['put', ],
        serializer_class=ReferralSerializer,
        url_name='update_product',
        url_path='product-update',
        serializer_include_fields=['product']
    )
    def update_product(self, request, *args, **kwargs):
        obj = self.get_object()
        previous_product = str(obj.product)
        if obj.status == COMPLETED:
            raise ValidationError('Product cannot be updated for converted lead.')

        serializer = self.update_referral(request, *args, **kwargs)
        obj.refresh_from_db()
        obj.update_commission()

        new_product = str(obj.product)
        self.add_notification(obj, previous_product, new_product)
        return Response(serializer.data)

    @staticmethod
    def add_notification(obj, prev_product, new_product):
        UserNotification.objects.create(**{
            'title': 'Product has been Updated',
            'sent_to': obj.referrer.user,
            'notification_type': INFO,
            'content': 'Your Product for lead {} at city {} has been updated to {}'.format(
                prev_product,
                str(obj.city),
                new_product
            )
        })

    @staticmethod
    def add_status_notification(obj, current_status, status):
        if status == COMPLETED:
            UserNotification.objects.create(**{
                'title': 'Congratulation Lead Completed',
                'sent_to': obj.referrer.user,
                'notification_type': POSITIVE,
                'content': 'Congratulation Your lead on {} for {} at city {} has been successfully converted'.format(
                    str(obj.product),
                    str(obj.referrer),
                    str(obj.city),
                )
            })
        else:
            UserNotification.objects.create(**{
                'title': 'Lead status Updated',
                'sent_to': obj.referrer.user,
                'notification_type': NEGATIVE if status == FAILED else POSITIVE,
                'content': 'Your lead on {} for {} at city {} has been changed from {} to {}'.format(
                    str(obj.product),
                    str(obj.referrer),
                    str(obj.city),
                    current_status,
                    status
                )
            })

    def update_referral(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data,
            partial=kwargs.pop('partial', False)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return serializer


class ReferralLogViewSet(CreateListViewSet):
    queryset = ReferralLog.objects.all()
    serializer_class = ReferralLogSerializer
    permission_class_mapper = {
        'create': [IsCompany | IsSuperUser],
        'list': [IsCompany | IsSuperUser]
    }
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ['referral', ]

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_company:
            qs = qs.filter(referral__company=self.request.user.company)
        return qs
