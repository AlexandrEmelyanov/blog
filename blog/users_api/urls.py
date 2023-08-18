from django.urls import path

from . import views

app_name = 'users_api'

urlpatterns = [
    path('api/v1/users/', views.UserAPIList.as_view()),
    path('api/v1/users/<int:pk>/', views.DetailUserAPIList.as_view()),
]
