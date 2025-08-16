from django.shortcuts import render, HttpResponse, redirect
from .models import Page, Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

def get_menu_tree(request):
    """Hierarhik menu strukturasini qaytaradi"""
    menus = Menu.objects.select_related('page').all()
    menu_dict = {}
    
    for menu in menus:
        if menu.parent_id not in menu_dict:
            menu_dict[menu.parent_id] = []
        menu_dict[menu.parent_id].append(menu)
    print(menu_dict)
    return HttpResponse(menu_dict)


def page_view(request, slug):
    try:
        page = Page.objects.get(slug=slug)
        if page.url:
            return redirect(page.url)
        return render(request, 'default.html', {'page': page})
    except Page.DoesNotExist:
        return render(request, 'default.html')