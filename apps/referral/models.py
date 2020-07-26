from django.db import models

from apps.company.models import Company
from apps.core.models import BaseModel
from apps.core.validators import validate_phone_number
from apps.referrer.models import Referrer


class Referral(BaseModel):
    referrer = models.ForeignKey(Referrer, related_name='referrals', on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name='referrals', on_delete=models.CASCADE)

    # Referral information
    name = models.CharField(max_length=255)
    phone_number = models.CharField(
        max_length=50,
        validators=[validate_phone_number]
    )

    def __str__(self):
        return f"{str(self.referrer)} refers to {self.name}"
