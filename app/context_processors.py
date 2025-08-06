from .models import Menu

def menu_context(request):
    return {
        'menu_items': Menu.objects.filter(is_active=True, parent__isnull=True).order_by('order')
    }
