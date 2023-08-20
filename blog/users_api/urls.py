from django.urls import path, include, re_path

from . import views

app_name = 'users-api'

urlpatterns = [
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # auth session and cookie

    path('api/v1/auth/', include('djoser.urls')),  # auth by token
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/v1/userslist/', views.UserAPIList.as_view()),
    path('api/v1/userdetail/<int:pk>/', views.DetailUserAPIList.as_view()),
]
