from django.shortcuts import render
from .models import Author, Book
from .serializer import AuthorSerializer, BookSerializer
from rest_framework import generics

# Create your views here.
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
