from django.contrib import admin
from .models import Program


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'participants', 'is_active', 'is_featured', 'created_at')
    list_filter = ('is_active', 'is_featured', 'created_at')
    search_fields = ('title', 'description', 'overview')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_editable = ('is_active',)
