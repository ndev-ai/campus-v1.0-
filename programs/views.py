from django.shortcuts import render, get_object_or_404
from .models import Program


def program_list(request):
    """Programs list view"""
    programs = Program.objects.filter(is_active=True)
    context = {
        'programs': programs
    }
    return render(request, 'programs_list.html', context)


def program_detail(request, slug):
    """Program detail view"""
    program = get_object_or_404(Program, slug=slug, is_active=True)
    context = {
        'program': program
    }
    return render(request, 'program_detail.html', context)
