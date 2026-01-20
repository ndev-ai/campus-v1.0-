from django.contrib import admin
from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email', 'order', 'is_active', 'is_featured', 'created_at')
    list_filter = ('is_active', 'is_featured', 'created_at')
    search_fields = ('name', 'role', 'email')
    list_editable = ('order', 'is_active', 'is_featured')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'role', 'email', 'image')
        }),
        ('Social Media', {
            'fields': ('linkedin', 'twitter')
        }),
        ('Settings', {
            'fields': ('order', 'is_active', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
