from django.urls import path

from . import views

app_name = 'category-api'

urlpatterns = [
    path('api/v1/categories/', views.CategoryAPIList.as_view()),
    path('api/v1/category/<int:pk>/', views.CategoryAPIDetail.as_view()),
]
