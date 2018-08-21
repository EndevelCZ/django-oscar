from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CustomConfig(AppConfig):
    label = 'custom'
    name = 'oscar.apps.custom'
    verbose_name = _('Custom')
