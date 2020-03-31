from django.shortcuts import render, get_object_or_404
from .models import Article


def home(request):
    context = {
        'title': 'main',
        'articles': Article.objects.filter(status='P')
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    context = {
        'article': get_object_or_404(Article, slug=slug, status='P'),

    }
    return render(request, 'blog/detail.html', context)
