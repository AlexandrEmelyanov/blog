from django.urls import path

from . import views

app_name = 'index'

urlpatterns = [
    path('', views.IndexView.as_view(), name='blog-home'),
    path('post/category/<int:category_id>/', views.IndexView.as_view(), name='category'),
    path('about/', views.about, name='about-club'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/user/<str:username>/', views.UserPostListView.as_view(), name='user-posts'),
    path('post/comment/delete/<int:comment_id>/', views.comment_delete, name='comment-delete'),
]
