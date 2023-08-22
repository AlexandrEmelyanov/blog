from django.urls import path

from . import views

app_name = 'users-api'

urlpatterns = [
    path('api/v1/userslist/', views.UserAPIList.as_view()),
    path('api/v1/userdetail/<int:pk>/', views.UserAPIDetail.as_view()),
]
