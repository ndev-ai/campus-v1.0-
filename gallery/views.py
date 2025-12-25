from django.shortcuts import render
from .models import Gallery


def gallery_list(request):
    """Gallery page view displaying all gallery images"""
    gallery_images = Gallery.objects.all()

    context = {
        'gallery_images': gallery_images,
    }
    return render(request, 'gallery.html', context)
