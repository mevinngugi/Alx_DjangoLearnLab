from django.urls import path
from .views import AuthorList, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    # Login, Logout views
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    
    # Redirects to home after login
    path('home/', TemplateView.as_view(template_name='api/home.html'), name='home'),

    # API urls for Author, Book AuthorList
    path('authors/', AuthorList.as_view(), name='author'),
    path('books/', ListView.as_view(), name='books'),

    # API URLs for the Book model to handle CRUD operations
    # DetailView
    path('books/<int:pk>/', DetailView.as_view(), name='book_detail'),

    # CreateView
    path('books/create/', CreateView.as_view(), name='new_book'),

    # UpdateView
    path('books/update/<int:pk>/', UpdateView.as_view(), name='update_book'),

    # DeleteView
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='delete_book'),

]