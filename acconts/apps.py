from django.apps import AppConfig


class AccontsConfig(AppConfig):
    name = 'acconts'

    def ready(self):
        import acconts.signals