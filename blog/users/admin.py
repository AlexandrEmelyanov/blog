from django.contrib import admin

from .models import User


@admin.register(User)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email')
