from django.contrib import admin

from .models import Comment, PostCategory, Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'category')
    fields = ('author', 'title', 'content', 'category')
    search_fields = ('author', 'title', 'category')
    ordering = ('date_posted',)


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_com', 'create_com', 'content')
    fields = ('author_com', 'post', 'content')
    ordering = ('create_com',)
