import random
import string

from django.contrib.auth import get_user_model
from django.db import models

from apps.common.models import City
from apps.core.models import BaseModel, SlugModel

User = get_user_model()


class Category(BaseModel, SlugModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=600, blank=True)

    def __str__(self):
        return self.name


class Company(BaseModel, SlugModel):
    parent = models.ForeignKey(
        'self',
        related_name='children',
        null=True,
        on_delete=models.SET_NULL
    )

    referral_code = models.CharField(max_length=50, unique=True, null=True)
    user = models.OneToOneField(User, related_name='company', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')

    category = models.ForeignKey(
        Category,
        related_name='companies',
        null=True,
        on_delete=models.SET_NULL
    )
    city = models.ForeignKey(
        City,
        related_name='companies',
        null=True,
        on_delete=models.SET_NULL
    )
    location = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Generate unique code for user build up from their full name and random integer like
        like if Foo Bar is full name the their username would be F****B (* could be any integer)
        """
        if not self.referral_code:
            self.referral_code = self.get_unique_code()
        return super().save(*args, **kwargs)

    def get_unique_code(self):
        count = 1
        code = self.get_random_code()
        while self.__class__.objects.filter(referral_code=code).exists():
            random_username = self.get_random_code() if count < 50 else self.get_random_code('')
            count += 1
        return code

    @staticmethod
    def get_random_letter():
        return random.choice(string.ascii_letters)

    def get_random_code(self, name=''):
        """
        Empty string will force to pick random first and second letter
        """
        name = name or self.name

        first_letter = ''
        last_letter = ''
        try:
            first_letter = name[0]
            last_letter = name[-1]
        except IndexError:
            first_letter = first_letter or self.get_random_letter()
            last_letter = last_letter or self.get_random_letter()

        random_letter = f'{first_letter.capitalize()}{random.randint(1000, 9999)}{last_letter.capitalize()}'
        return random_letter
