from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from apps.company.models import Company
from apps.core.models import BaseModel


User = get_user_model()


class Referrer(BaseModel):
    user = models.OneToOneField(
        User,
        related_name='referrer',
        on_delete=models.CASCADE
    )
    referred_by = models.ForeignKey(
        Company,
        null=True,
        related_name='referrers',
        on_delete=models.SET_NULL
    )
    dob = models.DateField(null=True)

    def __str__(self):
        return str(self.user)
