from django.contrib import admin
from django.utils.html import format_html
from .models import MaterialCategory, Material


@admin.register(MaterialCategory)
class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'materials_count')
    list_editable = ('order',)
    search_fields = ('name',)

    def materials_count(self, obj):
        return obj.materials.count()
    materials_count.short_description = "Materials"


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'file_type_badge', 'file_size', 'download_count', 'is_active', 'created_at')
    list_filter = ('category', 'file_type', 'is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    list_per_page = 20
    readonly_fields = ('file_size', 'download_count', 'created_at', 'updated_at')

    def file_type_badge(self, obj):
        colors = {
            'pdf': '#dc2626',
            'doc': '#2563eb',
            'xls': '#16a34a',
            'ppt': '#ea580c',
            'zip': '#7c3aed',
            'other': '#6b7280',
        }
        color = colors.get(obj.file_type, '#6b7280')
        return format_html(
            '<span style="background: {}; color: white; padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: 600;">{}</span>',
            color,
            obj.get_file_type_display()
        )
    file_type_badge.short_description = "Type"

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('File', {
            'fields': ('file', 'file_type', 'file_size')
        }),
        ('Statistics', {
            'fields': ('download_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_active',)
        }),
    )
