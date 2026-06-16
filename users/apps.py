from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals

        from django.contrib.auth.models import User
        from django.db.utils import OperationalError

        try:
            # Create superuser only if it doesn't exist
            if not User.objects.filter(username='gmiadmin').exists():
                User.objects.create_superuser(
                    username='gmiadmin',
                    email='admin@gmail.com',
                    password='GmiPass123!'
                )
                print("Superuser 'gmiadmin' created successfully.")
        except OperationalError:
            pass