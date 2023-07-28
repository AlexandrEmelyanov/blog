from django.contrib import admin
from .models import Posts


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    fields = ('author', 'title', 'content')
    search_fields = ('author', 'title')
    ordering = ('date_posted',)
