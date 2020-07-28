from exponent_server_sdk import DeviceNotRegisteredError
from exponent_server_sdk import PushClient
from exponent_server_sdk import PushMessage
from exponent_server_sdk import PushServerError

from apps.users.models import UserDevice


def send_push_message(
    token, title=None, body=None,
    extra=None, sound="default", ttl=None,
    expiration=None, priority=None,
    display_in_foreground=True, badge=None,
    category=None, channel_id=None
):
    try:
        response = PushClient().publish(
            PushMessage(
                to=token, data=extra,
                title=title, body=body,
                sound=sound, ttl=ttl,
                expiration=expiration,
                priority=priority, badge=badge,
                category=category,
                display_in_foreground=display_in_foreground,
                channel_id=channel_id
            )
        )

        try:
            response.validate_response()
        except DeviceNotRegisteredError:
            UserDevice.objects.filter(registration_id=token).update(is_active=False)
    except PushServerError:
        pass
