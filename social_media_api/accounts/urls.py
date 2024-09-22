from django.urls import path
from .views import RegisterCustomUserView, LoginCustomUserView
from rest_framework.authtoken import views


urlpatterns = [
    # Register Custom User
    path('register/', RegisterCustomUserView.as_view(), name="register"),

    # Login, Logout views
    # Planning to set the authentication to token
    path('login/', LoginCustomUserView.as_view(), name="register"),

    path('api-token-auth/', views.obtain_auth_token, name="api-token-auth"),
]