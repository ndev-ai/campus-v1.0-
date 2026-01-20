from django.contrib import admin
from .models import Event, Registration


class RegistrationInline(admin.TabularInline):
    """Inline admin for viewing registrations within Event admin"""
    model = Registration
    extra = 0
    readonly_fields = ('full_name', 'email', 'phone', 'note', 'created_at')
    can_delete = True

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location', 'is_featured', 'registration_count', 'created_at')
    list_filter = ('date', 'is_featured')
    search_fields = ('name', 'location')
    date_hierarchy = 'date'
    ordering = ('date',)
    inlines = [RegistrationInline]

    def registration_count(self, obj):
        """Display number of registrations for this event"""
        return obj.registrations.count()
    registration_count.short_description = 'Registrations'


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    """Admin interface for managing event registrations"""
    list_display = ('full_name', 'email', 'phone', 'event', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('full_name', 'email', 'phone', 'event__name')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        ('Event Information', {
            'fields': ('event',)
        }),
        ('Registrant Details', {
            'fields': ('full_name', 'email', 'phone', 'note')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
