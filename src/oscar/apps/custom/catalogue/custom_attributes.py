from django import forms
from oscar.apps.custom.catalogue.models import ColorChoice


def get_attribute_field(attribute):
    if attribute.type == 'entity' and attribute.code == 'color':
        return forms.ModelChoiceField(
            label=attribute.name,
            required=attribute.required,
            queryset=ColorChoice.objects.all()
        )

    return None
