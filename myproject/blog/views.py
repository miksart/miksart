from django.shortcuts import render
from .models import Article


def home(request):
    context = {
        'title': 'title test',
        'articles': Article.objects.all()
    }
    return render(request, 'blog/index.html', context)


def detail(request, slug):
    context = {
        'title': 'test detail',
        'article': Article.objects.get(slug=slug)
    }
    return render(request, 'blog/post.html', context)
