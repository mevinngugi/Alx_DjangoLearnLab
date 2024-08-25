from django.urls import path
from . import views
from django.core.exceptions import PermissionDenied
from django.http import Http404

def handle_permission_denied(request, exception):
    raise Http404("Page not found")

handler403 = handle_permission_denied

urlpatterns = [
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.edit_book, name="edit_book"),
    path("delete_book/", views.delete_book, name="delete_book"),
]