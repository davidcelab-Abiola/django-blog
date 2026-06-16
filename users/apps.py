from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals

        from django.contrib.auth.models import User

        try:
            # Only create if it doesn't exist (safer)
            User.objects.get_or_create(
                username='gmiadmin',
                defaults={
                    'email': 'admin@gmail.com',
                    'is_staff': True,
                    'is_superuser': True,
                }
            )
        except Exception:
            pass