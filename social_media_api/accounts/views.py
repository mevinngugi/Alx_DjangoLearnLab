from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginUserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, AllowAny


# Create your views here.
class RegisterCustomUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Custom Validation done by the serializer
            serializer.save()
            user = CustomUser.objects.get(username=serializer.data['username'])
            token = Token.objects.get(user=user.id)
            #import pdb; pdb.set_trace()
            return Response({'user': user.username, 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginCustomUserView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            logged_in_user = authenticate(username=username, password=password)
            if logged_in_user is not None:
                token = Token.objects.get(user=logged_in_user.id)
                return Response({'user': logged_in_user.username, 'token': token.key}, status=status.HTTP_201_CREATED)
        
            return Response({'error': 'Invalid credentials. Please check your username and password.'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow != request.user:
            request.user.following.add(user_to_follow)
            return Response({'status': 'success', 'message': f'You are now following {user_to_follow.username}'}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': 'An error occurred.'}, status=status.HTTP_400_BAD_REQUEST)


class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        if user_to_unfollow in request.user.following.all():
            request.user.following.remove(user_to_unfollow)
            return Response({'status': 'success', 'message': f'You have successfully unfollowed {user_to_unfollow}'}, status=status.HTTP_200_OK)
        return Response({'status': 'error', 'message': 'An error occurred.'}, status=status.HTTP_400_BAD_REQUEST)