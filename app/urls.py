from django.urls import path
from .views import home
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('same', get_menu_tree),
    path('<slug:slug>/', page_view, name='page_detail'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
