from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "blogaccountsite"

    def ready(self):
        import_module("blogaccountsite.receivers")
