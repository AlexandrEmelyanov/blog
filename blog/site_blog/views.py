from django.shortcuts import render
from .models import Posts


def index(request):
    context = {
        'title': 'Blog - Main',
        'posts': Posts.objects.all(),
    }
    return render(request, 'site_blog/home.html', context=context)


def about(request):
    context = {
        'title': 'Blog - about'
    }
    return render(request, 'site_blog/about.html', context=context)
