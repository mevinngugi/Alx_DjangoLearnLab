from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from rest_framework.authtoken import views

# Routes before using Routers

# urlpatterns = [
#     path('api/book_list', views.BookList.as_view(), name="book_list"),
#     path('api/book_list/<int:pk>/', views.BookDetail.as_view(), name="book_list"),
# ]

router = DefaultRouter()
router.register(r"book_all", BookViewSet, basename="book_all")

urlpatterns = [
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
    path("home/", TemplateView.as_view(template_name="base_templates/home.html"), name="home"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path('api-token-auth/', views.obtain_auth_token, name="api-token-auth"),
]