from django.shortcuts import render
from programs.models import Program
from news.models import News
from events.models import Event
from team.models import TeamMember


def home(request):
    """Home page view"""
    featured_programs = Program.objects.filter(is_active=True, is_featured=True)[:4]
    featured_news = News.objects.filter(is_published=True, is_featured=True)[:3]
    featured_events = Event.objects.filter(is_featured=True)[:3]
    featured_team = TeamMember.objects.filter(is_active=True, is_featured=True)[:4]

    context = {
        'programs': featured_programs,
        'news_list': featured_news,
        'events': featured_events,
        'team_members': featured_team,
    }
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    return render(request, 'about.html')
