from django.urls import path
from .views import AuthorList, BookList, BookDetailView, NewBookView, UpdateBookView, DeleteBookView
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
    path('books/', BookList.as_view(), name='books'),

    # API URLs for the Book model to handle CRUD operations
    # DetailView
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),

    # CreateView
    path('new_book/', NewBookView.as_view(), name='new_book'),

    # UpdateView
    path('update_book/<int:pk>/', UpdateBookView.as_view(), name='update_book'),

    # DeleteView
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),

]