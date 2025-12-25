from modeltranslation.translator import translator, TranslationOptions
from .models import TeamMember


class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('name', 'role')


translator.register(TeamMember, TeamMemberTranslationOptions)
