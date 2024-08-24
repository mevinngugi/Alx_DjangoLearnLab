from django.urls import path, include
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="relationship_app/home.html"), name="home"),
    path("list_books/", views.list_books, name="list_books"),
    #path("<int:book_id>/", views.detail, name="detail"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("signup/", views.register.as_view(), name="register"),
]