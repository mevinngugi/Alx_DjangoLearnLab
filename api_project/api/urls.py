from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Routes before using Routers

# urlpatterns = [
#     path('api/book_list', views.BookList.as_view(), name="book_list"),
#     path('api/book_list/<int:pk>/', views.BookDetail.as_view(), name="book_list"),
# ]

router = DefaultRouter()
router.register(r"book_all", BookViewSet, basename="book_all")

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]