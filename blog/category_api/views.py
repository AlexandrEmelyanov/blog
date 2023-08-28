from rest_framework import generics

from site_blog.models import PostCategory

from .serializers import CategorySerializer


class CategoryAPIList(generics.ListAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer


class CategoryAPIDetail(generics.RetrieveAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = CategorySerializer
