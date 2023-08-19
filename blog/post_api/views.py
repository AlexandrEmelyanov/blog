from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from .serializers import PostSerializer

from site_blog.models import Posts, PostCategory


class PostAPIView(generics.ListCreateAPIView):  # methods: get, post
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostAPIUpdate(generics.RetrieveUpdateAPIView):  # methods: put, patch
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostAPIDelete(generics.RetrieveDestroyAPIView):  # method: delete
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# class PostViewSet(viewsets.ModelViewSet):  # work with router
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer
#
#     @action(methods=['get'], detail=False)
#     def categories(self, request):
#         category = PostCategory.objects.all()
#         return Response({'categories': [cat.name for cat in category]})
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         category = PostCategory.objects.get(pk=pk)
#         return Response({'category': category.name})


