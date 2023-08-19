from rest_framework import permissions

from site_blog.models import Posts


class IsAuthorOrIsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        post = Posts.objects.get(pk=view.kwargs['pk'])
        return bool(request.user and request.user.is_staff) or bool(request.user == post.author)
