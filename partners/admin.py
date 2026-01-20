from django.contrib import admin
from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'website_url')
    list_editable = ('order', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Partner Information', {
            'fields': ('name', 'logo', 'website_url')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
