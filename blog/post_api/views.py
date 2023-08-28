from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from site_blog.models import Posts

from .permissions import IsAuthorOrIsAdminOrReadOnly, IsOwnerOrReadonly
from .serializers import PostSerializer


class PostAPIListPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'  # .../api/v1/post/.../page_size=n, when n <= max_page_size
    max_page_size = 100


class PostAPIList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PostAPIListPagination


class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadonly,)
    authentication_classes = (TokenAuthentication,)


class PostAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrIsAdminOrReadOnly,)
    authentication_classes = (TokenAuthentication,)

# !! if we're using router with ViewSet -> action for category returns:

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
