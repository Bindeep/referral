from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save

from apps.common.constants import NOTIFICATION_TYPE_CHOICES, INFO
from apps.core.models import BaseModel
from apps.core.utils.helpers import get_upload_path
from apps.core.utils.push_notification import send_push_message

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


class UserNotification(BaseModel):
    title = models.CharField(max_length=150)
    sent_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='sent_notifications')
    sent_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='notifications')
    content = models.TextField(blank=True)
    is_read = models.BooleanField(default=False)  # To mark notification as read
    notification_type = models.CharField(
        max_length=15,
        choices=NOTIFICATION_TYPE_CHOICES,
        default=INFO
    )

    def __str__(self):
        if self.sent_by:
            return f'Sent by {str(self.sent_by)} to {str(self.sent_to)} content {self.content}'
        return f'{str(self.sent_to)} content {self.content}'

    class Meta:
        ordering = ('is_read', '-created_at')


def send_push_notification(sender, instance, created, **kwargs):
    if created:
        receiver = instance.sent_to
        receiver_device = receiver.devices.filter(is_active=True).first()
        if receiver_device:
            send_push_message(
                receiver_device.registration_id,
                title=instance.title,
                body=instance.content
            )


def send_article_notifications(sender, instance, created, **kwargs):
    if created:
        UserNotification.objects.bulk_create([
            UserNotification(**{
                'title': instance.title,
                'sent_to': user,
                'notification_type': INFO,
                'content': instance.description
            }) for user in User.objects.all()
        ])


post_save.connect(send_push_notification, sender=UserNotification)
post_save.connect(send_article_notifications, sender=Article)
