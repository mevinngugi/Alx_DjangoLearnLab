from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
# Using the below import for the custom filter. 
from django_filters import rest_framework as advanced_filters

# Create your views here.

# Custom filter that returns partial search on title and author name
class PostListFilter(advanced_filters.FilterSet):
    title = advanced_filters.CharFilter(lookup_expr='icontains')
    content = advanced_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ('title', 'content')


class PostViewSet(viewsets.ModelViewSet):
    # Currently no one is able to get, put, post, delete if they don't have a token
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostListFilter
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at']
    # This will be the default ordering filter
    ordering = ['created_at']


class CommentViewSet(viewsets.ModelViewSet):
    # Currently no one is able to get, put, post, delete if they don't have a token
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    search_fields = ['content']
    ordering_fields = ['created_at']
    # This will be the default ordering filter
    ordering = ['created_at']
