from django.db import models
from django.db.models.signals import post_save

from apps.common.constants import INFO, POSITIVE
from apps.common.models import City, UserNotification
from apps.company.models import Company, Category
from apps.core.models import BaseModel
from apps.core.validators import validate_phone_number
from apps.referral.constants import STATUS_CHOICES, PENDING
from apps.referrer.models import Referrer


class Referral(BaseModel):
    referrer = models.ForeignKey(Referrer, related_name='referrals', on_delete=models.CASCADE)
    company = models.ForeignKey(
        Company,
        related_name='referrals',
        on_delete=models.SET_NULL,
        null=True
    )

    category = models.ForeignKey(
        Category,
        related_name='referrals',
        null=True,
        on_delete=models.SET_NULL
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

    amount = models.FloatField(null=True, default=None)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default=PENDING)

    def __str__(self):
        return f"{str(self.referrer)} refers to {self.name}"


def assign_company(sender, instance, created, **kwargs):
    if created:
        company = Company.objects.filter(city=instance.city, category=instance.category).first()
        instance.company = company
        instance.save()


def send_referral_notifications(sender, instance, created, **kwargs):
    if created:
        UserNotification.objects.create(**{
            'title': 'Your lead has been generated',
            'sent_to': instance.referrer.user,
            'notification_type': POSITIVE,
            'content': 'Your lead has been generated with category {} and city {}'.format(
                str(instance.category),
                str(instance.city)
            )
        })


post_save.connect(assign_company, sender=Company)
post_save.connect(send_referral_notifications, sender=Referral)
