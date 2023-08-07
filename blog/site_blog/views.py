from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import Posts
from common.views import TitleMixin


class IndexView(TitleMixin, ListView):
    template_name = 'site_blog/home.html'
    model = Posts
    ordering = ('-date_posted',)
    paginate_by = 5  # !!! don't work -- need added block paginator html !!!!
    title = 'Blog - Main'


class PostDetailView(TitleMixin, DetailView):
    model = Posts
    title = 'Blog - PostDetail'
    template_name = 'site_blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, TitleMixin, CreateView):
    model = Posts
    title = 'Blog - CreatePost'
    fields = ('title', 'content')
    success_message = 'Запись успешно создана.'
    template_name = 'site_blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, TitleMixin, DeleteView):
    model = Posts
    success_url = '/'
    title = 'Blog - PostDelete'
    success_message = 'Запись успешно удалена.'
    template_name = 'site_blog/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # bool


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
