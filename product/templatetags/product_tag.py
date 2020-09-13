from django import template
from product.models import Category, Product

register = template.Library()

# 2 спосіб вивести всі категорії
@register.simple_tag()
def get_categories():
    return Category.objects.all()

# 2 спосіб вивести і відрендирити разом з html
@register.inclusion_tag('product/tags/top_products.html')
def get_top_product(count=5):
    products = Product.objects.order_by("rating")[:count]
    return {"top_products": products}
