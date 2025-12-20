from django.shortcuts import render
from .models import Event


def event_list(request):
    """Events list view"""
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events_list.html', context)
