from django.contrib import admin
from django.utils.html import format_html
from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    """Admin configuration for Gallery model"""

    list_display = ('id', 'image_preview', 'created_at')
    readonly_fields = ('image_preview_large', 'created_at')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height: 50px; width: auto; object-fit: cover; border-radius: 4px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Preview"

    def image_preview_large(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 300px; width: auto; border-radius: 8px;" />', obj.image.url)
        return "-"
    image_preview_large.short_description = "Image Preview"

    fieldsets = (
        (None, {
            'fields': ('image', 'image_preview_large')
        }),
        ('Info', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
