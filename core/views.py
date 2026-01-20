from django.shortcuts import render
from programs.models import Program
from news.models import News
from events.models import Event
from partners.models import Partner


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
