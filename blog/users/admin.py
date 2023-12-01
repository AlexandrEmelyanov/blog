from django.contrib import admin

from .models import User, EmailVerification


@admin.register(User)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email')


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
