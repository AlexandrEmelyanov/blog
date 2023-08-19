from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import PostSerializer

from site_blog.models import Posts, PostCategory


class PostAPIView(generics.ListCreateAPIView):  # methods: get, post
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class PostAPIUpdate(generics.RetrieveUpdateAPIView):  # methods: put, patch
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class PostAPIDelete(generics.RetrieveDestroyAPIView):  # method: delete
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


# if we're using router with ViewSet -> action for category returns:

# from rest_framework.response import Response
# from rest_framework.decorators import action

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer
#
#     @action(methods=['get'], detail=False)  # return all cat
#     def categories(self, request):
#         category = PostCategory.objects.all()
#         return Response({'categories': [cat.name for cat in category]})
#
#     @action(methods=['get'], detail=True)  # return one cat
#     def category(self, request, pk=None):
#         category = PostCategory.objects.get(pk=pk)
#         return Response({'category': category.name})
