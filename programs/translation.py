from modeltranslation.translator import translator, TranslationOptions
from .models import Program


class ProgramTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'overview', 'objectives', 'impact', 'duration')


translator.register(Program, ProgramTranslationOptions)
