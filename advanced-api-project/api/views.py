from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics

# Create your views here.
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer