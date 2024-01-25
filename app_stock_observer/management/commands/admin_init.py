from django.conf import settings 

from django.core.management.base import BaseCommand

from django.contrib.auth.models import User


class Command(BaseCommand):

    def admin_init(self):
        admin = settings.DEFAULT_ADMIN
        super_user_qs = User.objects.filter(is_superuser=True)
        if super_user_qs.count() == 0:
            super_user = User.objects.create(
                username = admin['username'],
                email = admin['email'],
                password = admin['password'],
                is_active = True,
                is_staff = True,
                is_superuser = True
            )
            super_user.set_password(admin['password'])
            super_user.save()
            print(f'[==INFO==] Суперпользователь {admin["username"]} с паролем {admin["password"]} создан.')
        else:
            print('[==INFO==] Суперпользователь уже существует.')


    def handle(self, *args, **options):
        self.admin_init()
 