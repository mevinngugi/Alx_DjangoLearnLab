from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,  IsAdminUser
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        title_filter = self.request.query_params.get("title", None)
        if title_filter is not None:
            queryset = queryset.filter(title__contains=title_filter)
        return queryset

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = self.queryset.all()
        title_filter = self.request.query_params.get("title", None)
        if title_filter is not None:
            queryset = queryset.filter(title__contains=title_filter)
        return queryset
        
    def get(self, request):
        # Only authenticated users can view the list from model
        queryset = Book.objects.all()
        serializer_class = BookSerializer(queryset, many=True)
        return Response(serializer.data)
