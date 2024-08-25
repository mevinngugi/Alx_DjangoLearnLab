from django.urls import path, include
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView


from django.core.exceptions import PermissionDenied
from django.http import Http404

def handle_permission_denied(request, exception):
    raise Http404("Page not found")

handler403 = handle_permission_denied

urlpatterns = [
    path("", TemplateView.as_view(template_name="relationship_app/home.html"), name="home"),
    path("list_books/", views.list_books, name="list_books"),
    #path("<int:book_id>/", views.detail, name="detail"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    #Changed the register view from a class to a function to not have issues with UserCreationForm
    #path("signup/", views.register, name="register"),
    path("signup/", views.register, name="register"),
    path("admin/", views.admin_view, name="admin_view"),
    path("librarian/", views.librarian_view, name="librarian_view"),
    path("member/", views.member_view, name="member_view"),

    #Task 4
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.edit_book, name="edit_book"),
    path("delete_book/", views.delete_book, name="delete_book"),
]