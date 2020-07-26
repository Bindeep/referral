from django.contrib.auth import get_user_model
from django.db import models
from apps.core.models import BaseModel

# ***************************** Location *****************************
from apps.core.utils.helpers import get_upload_path


class AbstractLocationConstant(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(max_length=150, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Province(AbstractLocationConstant, BaseModel):
    country = models.ForeignKey(Country, on_delete=models.PROTECT)


class District(AbstractLocationConstant, BaseModel):
    province = models.ForeignKey(Province, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class City(AbstractLocationConstant):
    name = models.CharField(max_length=255, db_index=True)
    district = models.ForeignKey(District, on_delete=models.PROTECT,
                                 related_name='cities')
    district_name = models.CharField(blank=True, max_length=255)
    province = models.CharField(blank=True, max_length=255)
    country = models.CharField(blank=True, max_length=255)

    def save(self, *args, **kwargs):
        if not self.district_name:
            self.district_name = self.district.name
        if not self.province:
            self.province = self.district.province.name
        if not self.country:
            self.country = self.district.province.country.name
        super().save(*args, **kwargs)

    def __str__(self):
        full_location = '{}, {}, {}, {}'.format(
            self.name,
            self.district_name,
            self.province,
            self.country,
        )
        return full_location

    class Meta:
        unique_together = ('name', 'district')

    def get_related_info(self, district=True, province=True, country=True):
        info = {'city': self.name}
        if district:
            info['district'] = self.district_name
        if province:
            info['province'] = self.province
        if country:
            info['country'] = self.country
        return info

# ***************************** Location End *****************************


User = get_user_model()


class Article(BaseModel):
    created_by = models.ForeignKey(User, related_name='articles', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Below fields are optional
    image = models.ImageField(
        upload_to=get_upload_path,
        blank=True
    )
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
