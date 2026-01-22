from django.shortcuts import render, get_object_or_404
from django.http import FileResponse
from programs.models import Program
from news.models import News
from events.models import Event
from partners.models import Partner
from .models import Material, MaterialCategory


def home(request):
    """Home page view"""
    featured_programs = Program.objects.filter(is_active=True, is_featured=True)[:4]
    featured_news = News.objects.filter(is_published=True, is_featured=True)[:3]
    featured_events = Event.objects.filter(is_featured=True)[:3]
    partners = Partner.objects.filter(is_active=True)

    context = {
        'programs': featured_programs,
        'news_list': featured_news,
        'events': featured_events,
        'partners': partners,
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    return render(request, 'about.html')


def faq(request):
    """FAQ page view"""
    return render(request, 'faq.html')


def privacy(request):
    """Privacy policy page view"""
    return render(request, 'privacy.html')


def terms(request):
    """Terms of use page view"""
    return render(request, 'terms.html')


def materials(request):
    """Materials page view with downloadable files"""
    categories = MaterialCategory.objects.prefetch_related('materials').all()
    uncategorized_materials = Material.objects.filter(category__isnull=True, is_active=True)

    context = {
        'categories': categories,
        'uncategorized_materials': uncategorized_materials,
    }
    return render(request, 'materials.html', context)


def download_material(request, pk):
    """Download a material file and increment counter"""
    material = get_object_or_404(Material, pk=pk, is_active=True)
    material.download_count += 1
    material.save(update_fields=['download_count'])

    response = FileResponse(material.file.open('rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="{material.file.name.split("/")[-1]}"'
    return response
