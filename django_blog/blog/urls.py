from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    # Login, Logout views
    # Overriding the default path for login.html from templates/registration/login.html to blog/login.html by passing the template_name
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),

    #Nav bar redirects
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='home'),
    # Changing from TemplateView to a generic view in views.py
    #path('posts/', TemplateView.as_view(template_name='blog/posts.html'), name='posts'),
    path('posts/', views.PostListView.as_view(template_name='blog/posts.html'), name='posts'),
    # Using a function view for register because of the custom UserCreationForm 
    path('register/', views.register, name='register'),
    # Profile View
    path('profile/', views.profile, name='profile'),

    # Detail Post View
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Create Post View
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),

    # Update Post View
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_edit'),

    # Delete Post View
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # Add Comment View
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='add_comment'),

    # Update Comment View
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='edit_comment'),

    # Delete Comment View
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment'),

]