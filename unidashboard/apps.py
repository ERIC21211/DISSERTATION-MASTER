from django.apps import AppConfig


class UnidashboardConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "unidashboard"

    def ready(self):
        import unidashboard.signals  # Import signals.py to register the signal handler