# app/translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import News, VideoGallery, Event, Page, Faq

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


class VideoGalleryTranslationOptions(TranslationOptions):
    fields = ('title',)

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

class PageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class FaqTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


translator.register(News, NewsTranslationOptions)
translator.register(VideoGallery, VideoGalleryTranslationOptions)
translator.register(Event, EventTranslationOptions)
translator.register(Page, PageTranslationOptions)
translator.register(Faq, FaqTranslationOptions)
