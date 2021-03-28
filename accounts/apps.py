from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "appAccount"

    def ready(self):
        import accounts.signals
