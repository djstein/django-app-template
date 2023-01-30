from django.apps import AppConfig


class {{ app_slug|capitalize }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "{{ cookiecutter.app_slug }}"
