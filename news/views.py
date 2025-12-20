from django.shortcuts import render, get_object_or_404
from .models import News


def news_list(request):
    """News list view"""
    news = News.objects.filter(is_published=True)
    context = {
        'news_list': news
    }
    return render(request, 'news_list.html', context)


def news_detail(request, slug):
    """News detail view"""
    news = get_object_or_404(News, slug=slug, is_published=True)
    context = {
        'news': news
    }
    return render(request, 'news_detail.html', context)
