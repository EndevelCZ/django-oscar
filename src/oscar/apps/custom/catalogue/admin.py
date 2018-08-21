from django.contrib import admin
from oscar.core.loading import get_model

ColorChoice = get_model('custom_catalogue', 'ColorChoice')

admin.site.register(ColorChoice)
