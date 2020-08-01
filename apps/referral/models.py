from django.db import models
from django.db.models.signals import post_save

from apps.common.constants import POSITIVE
from apps.common.models import City, UserNotification
from apps.company.models import Company, Product
from apps.core.models import BaseModel
from apps.core.validators import validate_phone_number
from apps.referral.constants import STATUS_CHOICES, PENDING
from apps.referrer.models import Referrer


class Referral(BaseModel):
    referrer = models.ForeignKey(
        Referrer,
        related_name='referrals',
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        related_name='referrals',
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        Product,
        related_name='referrals',
        on_delete=models.CASCADE
    )

    city = models.ForeignKey(
        City,
        related_name='referrals',
        null=True,
        on_delete=models.SET_NULL
    )
    remarks = models.TextField(blank=True, default='')

    # Referral information
    name = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=50,
        validators=[validate_phone_number]
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default=PENDING)

    commission_amount = models.FloatField(default=0)

    def __str__(self):
        return f"{str(self.referrer)} refers to {self.name}"


class ReferralLog(BaseModel):
    # to add logs for referral
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name='logs')
    note = models.TextField()

    def __str__(self):
        return self.note


def assign_company(sender, instance, created, **kwargs):
    if created:
        company = Company.objects.filter(
            cities=instance.city,
            products=instance.product
        ).distinct().first()
        if company:
            instance.company = company
            instance.commission_amount = instance.product.commission_amount
            instance.save()


def send_referral_notifications(sender, instance, created, **kwargs):
    if created:
        UserNotification.objects.create(**{
            'title': 'Your lead has been generated',
            'sent_to': instance.referrer.user,
            'notification_type': POSITIVE,
            'content': 'Your lead {} has been generated for product {} and city {}'.format(
                instance.name,
                str(instance.product),
                str(instance.city)
            )
        })


post_save.connect(assign_company, sender=Referral)
post_save.connect(send_referral_notifications, sender=Referral)
