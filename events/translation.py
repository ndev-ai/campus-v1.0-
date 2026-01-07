from modeltranslation.translator import translator, TranslationOptions
from .models import Event


class EventTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'description')


translator.register(Event, EventTranslationOptions)
