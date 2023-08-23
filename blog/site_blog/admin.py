from django.contrib import admin

from .models import Comment, PostCategory, Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted', 'category', 'rating_post')
    fields = ('author', 'title', 'content', 'category')
    search_fields = ('author', 'title', 'category')
    ordering = ('-date_posted', '-title')
    list_editable = ('category',)
    list_per_page = 8

    @admin.display(ordering='comments', description='Rating')
    def rating_post(self, post: Posts):
        if post.comments.count() < 3:
            return 'Не популярный'
        return 'Популярный'


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post_counter', 'rating_category')
    fields = ('name',)
    readonly_fields = ('post_counter',)
    ordering = ('id', 'name')
    list_editable = ('name',)
    list_per_page = 8

    @admin.display(ordering='post_counter', description='Rating')  # calculated field
    def rating_category(self, category: PostCategory):
        if category.post_counter < 3:
            return 'Не популярная'
        if 3 <= category.post_counter <= 6:
            return 'Средняя'
        return 'Популярная'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_com', 'create_com', 'content')
    fields = ('author_com', 'post', 'content')
    ordering = ('-create_com', 'post')
    list_per_page = 8
