from django.apps import AppConfig


class MyConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'apps.app'
    label = 'apps_app'