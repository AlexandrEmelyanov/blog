from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import (HttpResponseRedirect, get_object_or_404,
                              redirect, render)
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from users.models import User

from .forms import CommentForm
from .models import Comment, Posts


class IndexView(TitleMixin, ListView):
    template_name = 'site_blog/home.html'
    model = Posts
    ordering = ('-date_posted',)
    paginate_by = 5
    title = 'Blog - Main'

    def get_context_data(self, **kwargs):  # for cache category
        context = super().get_context_data(**kwargs)
        context['category_id'] = self.kwargs.get('category_id')
        return context

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


class UserPostListView(TitleMixin, ListView):
    model = Posts
    paginate_by = 5
    title = 'Blog - UserPosts'
    template_name = 'site_blog/user_posts.html'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(TitleMixin, DetailView):
    model = Posts
    title = 'Blog - PostDetail'
    template_name = 'site_blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        post = self.get_object()

        if request.user.is_authenticated:
            if comment_form.is_valid():
                content = request.POST.get('content')
                new_comment = Comment.objects.create(content=content, post=post, author_com=request.user)
                new_comment.save()
                messages.success(request, 'Комментарий успешно добавлен.')
                return redirect('index:post-detail', pk=post.id)
            else:
                messages.error(
                    request,
                    'Произошла ошибка при добавлении комментария. Пожалуйста, проверьте введенные данные и попробуйте снова'
                )
                return redirect('index:post-detail', pk=post.id)
        else:
            messages.warning(request, 'Авторизуйтесь, чтобы комментировать записи.')
            return redirect('users:login')


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


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, TitleMixin, UpdateView):
    model = Posts
    fields = ('title', 'content')
    title = 'Blog - PostUpdate'
    success_message = 'Запись успешно изменена.'
    success_url = '/'
    template_name = 'site_blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def comment_delete(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    messages.success(request, 'Комментарий успешно удален.')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def about(request):
    context = {
        'title': 'Blog - about'
    }
    return render(request, 'site_blog/about.html', context=context)
