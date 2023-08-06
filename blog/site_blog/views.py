from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Posts
from common.views import TitleMixin


class IndexView(TitleMixin, ListView):
    template_name = 'site_blog/home.html'
    model = Posts
    ordering = ('-date_posted',)
    paginate_by = 4
    title = 'Blog - Main'


class PostDetailView(DetailView):
    model = Posts
    title = 'Blog - PostDetail'
    template_name = 'site_blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Posts
    title = 'Blog - CreatePost'
    fields = ('title', 'content')
    success_message = 'Запись успешно создана.'
    template_name = 'site_blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


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
