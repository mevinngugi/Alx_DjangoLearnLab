from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

from .models import Book
# Create your views here.

# Did not create the html files 
@permission_required("bookshelf.can_create", raise_exception=True)
def add_book(request):
    return render(request, "bookshelf/add_book.html")

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    return render(request, "bookshelf/book_list.html")

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book(request):
    return render(request, "bookshelf/edit_book.html")

@permission_required("bookshelf.can_delete", raise_exception=True)
def delete_book(request):
    return render(request, "bookshelf/delete_book.html")