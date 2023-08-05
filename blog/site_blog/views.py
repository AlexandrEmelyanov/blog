from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Posts
from common.views import TitleMixin


class IndexView(TitleMixin, ListView):
    template_name = 'site_blog/home.html'
    model = Posts
    ordering = ('-date_posted',)
    paginate_by = 4
    title = 'Blog - Main'


def about(request):
    context = {
        'title': 'Blog - about'
    }
    return render(request, 'site_blog/about.html', context=context)


# FBV
# def index(request):
#     context = {
#         'title': 'Blog - Main',
#         'posts': Posts.objects.all(),
#     }
#     return render(request, 'site_blog/home.html', context=context)
