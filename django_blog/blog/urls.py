from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    # Login, Logout views
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),

    # Redirects to home after login
    path('home/', TemplateView.as_view(template_name='blog/home.html'), name='home'),

    #Nav bar redirects
    path('posts/', TemplateView.as_view(template_name='blog/posts.html'), name='posts'),
    # Using a function view for register because of the custom UserCreationForm 
    path('register/', views.register, name='register'),

    # Profile View
    path('profile/', views.profile, name='profile'),

]