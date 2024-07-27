from django.db.models import Q
from django.shortcuts import render

from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from rest_framework import filters

from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView

from main.models import PostModel
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import PostLimitPagination




class PostCreateView(CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    
class PostDetailView(RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'


class PostUpdateView(RetrieveUpdateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PostDeleteView(DestroyAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'pk'   



class PostApiView(ListAPIView):
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_filds = ['name', 'body']
    pagination_class = PostLimitPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = PostModel.objects.all()

        query = self.request.GET.get("q")
        if query:
            queryset_list = PostModel.objects.filter(
                Q(name__icontains=query)
                ).distinct()

        # else:
        #     qs = PostModel.objects.all()

        return queryset_list