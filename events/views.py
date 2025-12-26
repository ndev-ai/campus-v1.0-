from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Event


def event_list(request):
    """Events list view with pagination"""
    events_queryset = Event.objects.all()
    paginator = Paginator(events_queryset, 6)  # 6 items per page

    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    context = {
        'events': events
    }
    return render(request, 'events_list.html', context)
