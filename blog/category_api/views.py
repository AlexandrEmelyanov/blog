from rest_framework import generics

from .serializers import CategorySerializer

from site_blog.models import PostCategory


class CategoryAPIList(generics.ListAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIDetail(generics.RetrieveAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer

