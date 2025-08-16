from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.static import serve
from django.views.i18n import set_language
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('i18n/', set_language, name='set_language'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 