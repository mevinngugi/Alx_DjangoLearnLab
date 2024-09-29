from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeedView, LikePostView, UnLikePostView
from django.urls import path 

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', UnLikePostView.as_view(), name='unlike_post'),
    path('feed/', UserFeedView.as_view(), name='user_feed'),
]

urlpatterns += router.urls