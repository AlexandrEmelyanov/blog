from django.urls import path
from . import views


app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='blog-home'),
    path('about/', views.about, name='about-club'),
]