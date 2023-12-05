from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path

from .yasg import urlpatterns as api_doc_urls

admin.site.index_title = 'Администрирование блога'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('site_blog.urls', namespace='index')),
    path('users/', include('users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),

    # api
    path('', include('users_api.urls', namespace='users-api')),
    path('', include('post_api.urls', namespace='post-api')),
    path('', include('comment_api.urls', namespace='comment-api')),
    path('', include('category_api.urls', namespace='category-api')),

    # auth_api
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # auth session and cookie
    path('api/v1/auth/', include('djoser.urls')),  # auth by token
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

# api_doc
urlpatterns += api_doc_urls

if settings.DEBUG:
    urlpatterns.append(path('__debug__', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
