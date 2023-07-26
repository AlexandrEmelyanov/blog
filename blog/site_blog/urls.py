from django.urls import path
from . import views


app_name = 'index'

urlpatterns = [
    path('', views.index, name='blog-home'),
    path('about/', views.about, name='about-club'),
]