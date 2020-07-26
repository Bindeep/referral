from django.db import models
from django.db.models.signals import post_save

from apps.common.models import City
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

    # Referral information
    name = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=50,
        validators=[validate_phone_number]
    )

    amount = models.FloatField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default=PENDING)

    def __str__(self):
        return f"{str(self.referrer)} refers to {self.name}"


def assign_company(sender, instance, created, **kwargs):
    if created:
        company = Company.objects.filter(city=instance.city, category=instance.category).first()
        instance.company = company
        instance.save()


post_save.connect(assign_company, sender=Company)
