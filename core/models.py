from django.db import models


class MaterialCategory(models.Model):
    """Category for organizing materials"""
    name = models.CharField(max_length=100, verbose_name="Category Name")
    description = models.TextField(blank=True, verbose_name="Description")
    order = models.IntegerField(default=0, verbose_name="Display Order")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Material Category"
        verbose_name_plural = "Material Categories"

    def __str__(self):
        return self.name


class Material(models.Model):
    """Downloadable materials and templates"""
    FILE_TYPE_CHOICES = [
        ('pdf', 'PDF Document'),
        ('doc', 'Word Document'),
        ('xls', 'Excel Spreadsheet'),
        ('ppt', 'PowerPoint'),
        ('zip', 'ZIP Archive'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField(blank=True, verbose_name="Description")
    category = models.ForeignKey(
        MaterialCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='materials',
        verbose_name="Category"
    )
    file = models.FileField(upload_to='materials/', verbose_name="File")
    file_type = models.CharField(
        max_length=10,
        choices=FILE_TYPE_CHOICES,
        default='pdf',
        verbose_name="File Type"
    )
    file_size = models.CharField(max_length=20, blank=True, verbose_name="File Size")
    download_count = models.IntegerField(default=0, verbose_name="Download Count")
    is_active = models.BooleanField(default=True, verbose_name="Active")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.file:
            # Calculate file size
            size = self.file.size
            if size < 1024:
                self.file_size = f"{size} B"
            elif size < 1024 * 1024:
                self.file_size = f"{size / 1024:.1f} KB"
            else:
                self.file_size = f"{size / (1024 * 1024):.1f} MB"
        super().save(*args, **kwargs)
