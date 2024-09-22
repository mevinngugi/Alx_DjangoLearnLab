from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
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
    permission_classes = [IsOwnerOrReadOnly]
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostListFilter
    search_fields = ['title', 'content']
    ordering_fields = ['title', 'created_at']
    # This will be the default ordering filter
    ordering = ['created_at']


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    search_fields = ['content']
    ordering_fields = ['created_at']
    # This will be the default ordering filter
    ordering = ['created_at']
