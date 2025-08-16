from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin
from .models import Page, Menu, News, Block, Faq, Contact, VideoGallery

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'date_created')

@admin.register(VideoGallery)
class VideoGalleryAdmin(TranslationAdmin):
    list_display = ('title', 'date_created')

admin.site.register(Page)
admin.site.register(Block)
admin.site.register(Faq)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_created',)
    search_fields = ('name', 'email', 'message')

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_filter = ['is_active', 'parent']
    search_fields = ['title']

    

    
    
    