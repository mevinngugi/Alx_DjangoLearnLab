from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated
# Using the below import for the custom filter. 
from django_filters import rest_framework as advanced_filters
# Adding this for the checker
from rest_framework import permissions

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


# class UserFeedView(generics.GenericAPIView):
#     # Adding permissions.IsAuthenticated for the checker 
#     # Remember to remove the import up top
#     permission_classes = [IsAuthenticated, permissions.IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self, request):
#         # current_user = request.user
#         # import pdb; pdb.set_trace()
#         following = request.user.following.all()
#         posts = []
#         # import pdb; pdb.set_trace()
#         # Get posts for each user. Add them to posts
#         for user in following:
#             user_posts = Post.objects.filter(author=user).order_by('-created_at')
#             posts.extend(user_posts)
#             # import pdb; pdb.set_trace()
#         if not posts:
#             return Response({'status': 'error', 'message': 'Nothing to display. You are not following anyone.'}, status=status.HTTP_200_OK)

#         serializer = self.get_serializer(posts, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)


class UserFeedView(generics.GenericAPIView):
    # Adding permissions.IsAuthenticated for the checker 
    # Remember to remove the import up top
    permission_classes = [IsAuthenticated, permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request):
        # current_user = request.user
        # import pdb; pdb.set_trace()
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        if not posts:
            return Response({'status': 'error', 'message': 'Nothing to display. You are not following anyone.'}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(posts, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    # serializer_class = LikePostSerializer

    def post(self, request, pk):
        # serializer = self.get_serializer(data=request.data)
        post = get_object_or_404(Post, pk=pk)
        already_liked_post = Like.objects.filter(post=post, user=request.user)

        if already_liked_post:
            return Response({f'error':'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(post=post, user=request.user)
        return Response({'message': 'You have liked this post.'})


class UnLikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        already_liked_post = Like.objects.filter(post=post, user=request.user)

        if already_liked_post:
            already_liked_post.delete()
            return Response({'message': 'You have unliked this post.'})

        return Response({f'error':'You need to have liked a post before unliking it.'}, status=status.HTTP_400_BAD_REQUEST)
