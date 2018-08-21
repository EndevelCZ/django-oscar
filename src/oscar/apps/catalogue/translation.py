from modeltranslation.translator import translator, TranslationOptions
from oscar.core.loading import get_model

Product = get_model('catalogue', 'Product')

class ProductTranslationOptions(TranslationOptions):
    fields = ('title','description',)

translator.register(Product, ProductTranslationOptions)
