from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'created_at')
    list_filter = ('date',)
    search_fields = ('name', 'location')
    date_hierarchy = 'date'
    ordering = ('date',)
