from .models import Menu
from datetime import datetime

def menu_context(request):
    return {
        'menu_items': Menu.objects.filter(
            parent=None, 
            is_active=True
        ).prefetch_related('children')
    }


def currently_year(request):
    current_year = datetime.now().year
    return {'current_year': current_year}