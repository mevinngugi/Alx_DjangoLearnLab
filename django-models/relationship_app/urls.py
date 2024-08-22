from django.urls import path
from . import views

app_name = "relationship_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("book_list/", views.book_list, name="book_list"),
    #path("<int:book_id>/", views.detail, name="detail"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail")
]