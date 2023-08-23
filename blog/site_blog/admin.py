from django.contrib import admin

from .models import Comment, PostCategory, Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'category')
    fields = ('author', 'title', 'content', 'category')
    search_fields = ('author', 'title', 'category')
    ordering = ('-date_posted', '-title')
    list_editable = ('category',)
    list_per_page = 8


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    fields = ('name',)
    ordering = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_com', 'create_com', 'content')
    fields = ('author_com', 'post', 'content')
    ordering = ('-create_com', 'post')
    list_per_page = 8
