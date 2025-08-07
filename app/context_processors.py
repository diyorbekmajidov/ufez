from .models import Menu
from datetime import datetime

def menu_context(request):
    return {
        'menu_items': Menu.objects.filter(is_active=True, parent__isnull=True).order_by('order')
    }

def currently_year(request):
    currently_year = datetime.now().year
    return {"currently_year":currently_year}
