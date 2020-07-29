from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.constants import POSITIVE, NEGATIVE
from apps.common.models import UserNotification
from apps.core.permissions import IsCompany, IsSuperUser, IsReferrer
from apps.core.viewsets import CreateListRetrieveUpdateViewSet
from apps.referral.api.v1.serializers import ReferralSerializer
from apps.referral.constants import FAILED, COMPLETED
from apps.referral.models import Referral


class ReferralViewSet(CreateListRetrieveUpdateViewSet):
    permission_class_mapper = {
        'create': [IsReferrer],
        'list': [IsReferrer | IsCompany | IsSuperUser],
        'retrieve': [IsReferrer | IsCompany | IsSuperUser],
        'update': [IsCompany | IsSuperUser],
    }
    filter_backends = (DjangoFilterBackend, )
    filter_fields = ['status']

    queryset = Referral.objects.all()
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
            return ['amount', 'status']
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
        url_name='update_amount',
        url_path='amount-update',
        serializer_include_fields=['amount']
    )
    def update_amount(self, request, *args, **kwargs):
        serializer = self.update_referral(request, *args, **kwargs)
        obj = self.get_object()
        if obj.status != COMPLETED:
            return Response({'error': 'Status should be in converted state.'}, status=status.HTTP_400_BAD_REQUEST)
        if obj.amount is None:
            self.add_amount_notification(
                obj,
                serializer.data.get('amount')
            )
            return self.update(request, args, kwargs)
        else:
            return Response({'error': 'Amount has already been updated once.'}, status=status.HTTP_400_BAD_REQUEST)

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

    @staticmethod
    def add_status_notification(obj, current_status, status):
        UserNotification.objects.create(**{
            'title': 'Lead status Updated',
            'sent_to': obj.referrer.user,
            'notification_type': NEGATIVE if status == FAILED else POSITIVE,
            'content': 'Your lead status on {} with {} category at city {} has been changed from {} to {}'.format(
                obj.name,
                str(obj.category),
                str(obj.city),
                current_status,
                status
            )
        })

    @staticmethod
    def add_amount_notification(obj, amount):
        UserNotification.objects.create(**{
            'title': 'Lead amount Updated',
            'sent_to': obj.referrer.user,
            'notification_type': POSITIVE,
            'content': 'Congratulations, You have earned Rs. {} from your lead on {} with {} at {}'.format(
                amount,
                obj.name,
                str(obj.category),
                str(obj.city),

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
