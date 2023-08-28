from django.urls import path

from . import views

app_name = 'post-api'

# router = routers.SimpleRouter()
# router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('api/v1/post/', views.PostAPIList.as_view()),
    path('api/v1/post/<int:pk>', views.PostAPIUpdate.as_view()),
    path('api/v1/postdelete/<int:pk>', views.PostAPIDelete.as_view()),

    # path('api/v1/', include(router.urls)),
]
