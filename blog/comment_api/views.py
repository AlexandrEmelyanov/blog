from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CommentSerializer
from .permissions import IsAuthorOrIsAdminOrReadOnly

from site_blog.models import Comment


class CommentAPIListPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommentAPIList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    pagination_class = CommentAPIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentAPIDetail(generics.RetrieveAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentAPIDelete(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsAuthorOrIsAdminOrReadOnly,)
