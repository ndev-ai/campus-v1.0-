from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Event


@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ('name', 'date', 'location', 'is_featured', 'created_at')
    list_filter = ('date', 'is_featured')
    search_fields = ('name', 'location')
    date_hierarchy = 'date'
    ordering = ('date',)

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
