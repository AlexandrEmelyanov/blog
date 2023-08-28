from django.contrib import admin
from django.db import models
from django.db.models import QuerySet

from .models import Comment, PostCategory, Posts


class RatingPostFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<3', 'Не популярный'),
            ('>=3', 'Популярный'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<3':
            return queryset.annotate(comment_count=models.Count('comments')).filter(comment_count__lt=3)
        elif self.value() == '>=3':
            return queryset.annotate(comment_count=models.Count('comments')).filter(comment_count__gte=3)
        return queryset


class RatingCategoryFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<3', 'Не популярная'),
            ('от 3 до 6', 'Средняя'),
            ('>6', 'Популярная'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<3':
            return queryset.filter(post_counter__lt=3)
        elif self.value() == 'от 3 до 6':
            return queryset.filter(post_counter__gte=3).filter(post_counter__lt=7)
        elif self.value() == '>6':
            return queryset.filter(post_counter__gt=6)
        return queryset


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'category', 'rating_post')
    fields = ('author', 'category', 'title', 'content',)
    search_fields = ('title__istartswith',)
    ordering = ('-date_posted', '-title')
    list_editable = ('category',)
    list_per_page = 8
    list_filter = ('category', RatingPostFilter)

    @admin.display(ordering='comments', description='rating')
    def rating_post(self, post: Posts):
        if post.comments.count() < 3:
            return 'Не популярный'
        return 'Популярный'


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post_counter', 'rating_category')
    fields = ('name',)
    search_fields = ('name',)
    readonly_fields = ('post_counter',)
    ordering = ('id', 'name')
    list_editable = ('name',)
    list_per_page = 8
    list_filter = (RatingCategoryFilter,)

    @admin.display(ordering='post_counter', description='Rating')  # calculated field
    def rating_category(self, category: PostCategory):
        if category.post_counter < 3:
            return 'Не популярная'
        elif 3 <= category.post_counter <= 6:
            return 'Средняя'
        return 'Популярная'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_com', 'create_com', 'content')
    fields = ('author_com', 'post', 'content')
    ordering = ('-create_com', 'post')
    list_per_page = 8
    search_fields = ('content',)
