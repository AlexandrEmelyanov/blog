from django.urls import path

from . import views

app_name = 'comment-api'

urlpatterns = [
    path('api/v1/comment/', views.CommentAPIList.as_view()),
    path('api/v1/comment/<int:pk>/', views.CommentAPIDetail.as_view()),
    path('api/v1/commentdelete/<int:pk>/', views.CommentAPIDelete.as_view()),
]
