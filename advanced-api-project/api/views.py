from django.shortcuts import render, get_object_or_404
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, DjangoModelPermissions



# Create your views here.
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ListView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])

class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])

class CreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Custom Validation to check if there is a record of book title by the author already created 
            passed_title = serializer.validated_data['title']
            passed_author = serializer.validated_data['author']
            filter_for_existing_book = Book.objects.filter(title=passed_title.title(), author=passed_author).first()
            if filter_for_existing_book:
                raise ValidationError(f'The book {passed_title.title()} by {passed_author} already exists.')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Custom Validation to check if there is a record of book title by the author already created 
            passed_title = serializer.validated_data['title']
            passed_author = serializer.validated_data['author']
            filter_for_existing_book = Book.objects.filter(title=passed_title.title(), author=passed_author).first()
            if filter_for_existing_book:
                raise ValidationError(f'The book {passed_title.title()} by {passed_author} already exists.')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])