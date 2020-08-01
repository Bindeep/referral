from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Dummy Superuser."

    def handle(self, *args, **options):
        if not User.objects.filter(is_superuser=True).exists():
            user = User()
            user.email = 'admin@gmail.com'
            user.phone = '123456789'
            user.full_name = 'Admin'
            user.is_superuser = True
            user.is_staff = True
            user.set_password('hellonepal')
            user.save()

            print(f"""
            Successfully Created superuser with
            email: {user.email},
            phone: {user.phone},
            pw: hellonepal,
            """)
        else:
            user = User.objects.filter(is_superuser=True).first()
            print('email: {}, phone: {}'.format(user.email, user.phone))
