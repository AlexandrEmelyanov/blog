from django.shortcuts import render


def index(request):
    context = {
        'title': 'Blog - main'
    }
    return render(request, 'site_blog/home.html', context=context)


def about(request):
    context = {
        'title': 'Blog - about'
    }
    return render(request, 'site_blog/about.html', context=context)
