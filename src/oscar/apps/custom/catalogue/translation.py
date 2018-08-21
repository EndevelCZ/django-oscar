from modeltranslation.translator import translator, TranslationOptions
from .models import ColorChoice

class ColorChoiceTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(ColorChoice, ColorChoiceTranslationOptions)
