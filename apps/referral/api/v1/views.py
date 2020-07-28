from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.constants import POSITIVE
from apps.common.models import UserNotification
from apps.core.permissions import IsCompany, IsSuperUser, IsReferrer
from apps.core.viewsets import CreateListRetrieveUpdateViewSet
from apps.referral.api.v1.serializers import ReferralSerializer
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

    current_status = ''
    next_status = ''

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
        return self.update(request, args, kwargs)

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
        self.current_status = obj.status
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data,
            partial=kwargs.pop('partial', False)
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @staticmethod
    def add_referrer_notification(user):
        UserNotification.objects.create(**{
            'title': 'Your lead has been generated',
            'sent_to': user,
            'notification_type': POSITIVE,
            'content': 'Your lead has been generated with'
        })
