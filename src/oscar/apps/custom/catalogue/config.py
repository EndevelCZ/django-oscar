from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CatalogueCustomConfig(AppConfig):
    label = 'custom_catalogue'
    name = 'oscar.apps.custom.catalogue'
    verbose_name = _('Catalogue')
