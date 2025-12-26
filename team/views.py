from django.shortcuts import render
from django.core.paginator import Paginator
from .models import TeamMember


def team_list(request):
    """View to display list of all active team members with pagination"""
    team_queryset = TeamMember.objects.filter(is_active=True)
    paginator = Paginator(team_queryset, 8)  # 8 items per page

    page_number = request.GET.get('page')
    team_members = paginator.get_page(page_number)

    context = {
        'team_members': team_members
    }
    return render(request, 'team_list.html', context)
