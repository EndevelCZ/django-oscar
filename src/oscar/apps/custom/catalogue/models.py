from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class ColorChoice(models.Model):
    name = models.CharField(_('Název barvy'), max_length=32)
    hex_code = models.CharField(_('HTML kód'), max_length=6)
    image = models.ImageField(_('Obrázek'), help_text=_('Obrázek musí mít čtvercový formát, maximální velikost je 64x64 px'))

    class Meta:
        verbose_name = _('Barva')
        verbose_name_plural = _('Barvy')


    def clean(self):
        errors = {}

        if not self.pk and self.image:
            if self.image.width != self.image.height:
                errors['image'] = _('Obrázek musí mít čtvercový formát')

            if self.image.width > 64:
                errors['image'] = _('Maximální velikost obrázku je 64x64 px')

        if errors:
            raise ValidationError(errors)

        return super().clean()
