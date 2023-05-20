from django.template import Library
from home.models import Categorie

register = Library()

@register.simple_tag
def global_category():
    categories = Categorie.objects.all()
    return categories
