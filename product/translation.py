from modeltranslation.translator import register, TranslationOptions
from .models import Category, Product, Action, Tag

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug')

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', 'description')

@register(Action)
class ActionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name',)