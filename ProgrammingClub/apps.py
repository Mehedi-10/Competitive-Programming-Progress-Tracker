from django.apps import AppConfig


class ProgrammingclubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ProgrammingClub'
    def ready(self):
        from .tests import start
        start()
