from django import template
from app.models import Menu 

register = template.Library()

@register.inclusion_tag('partials/menu_item.html')
def render_menu_item(item):
    return {'item': item}
