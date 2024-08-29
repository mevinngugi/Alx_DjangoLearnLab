from django.urls import path
from . import views


urlpatterns = [
    path('api/book_list', views.BookList.as_view(), name="book_list"),
    path('api/book_list/<int:pk>/', views.BookDetail.as_view(), name="book_list"),
]