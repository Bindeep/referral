from django.contrib.auth import get_user_model
from django.db import models
from apps.core.models import BaseModel
from apps.core.utils.helpers import get_upload_path


User = get_user_model()


class City(BaseModel):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name


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
