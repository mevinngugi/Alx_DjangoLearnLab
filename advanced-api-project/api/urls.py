from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    # Login, Logout views
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    
    # Redirects to home after login
    path('home/', TemplateView.as_view(template_name="api/home.html"), name="home"),
]