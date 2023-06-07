from django.apps import AppConfig

class AcmsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acms'

    def ready(self):
        import acms.signals