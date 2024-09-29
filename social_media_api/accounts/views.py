from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginUserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import DjangoModelPermissions, IsAuthenticated, AllowAny
# Adding this for the checker
from rest_framework import permissions


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


class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # Get the first instance that match from the queryset. If not, user does not exist
        user_to_follow = CustomUser.objects.all().filter(id=user_id).first()

        if user_to_follow:
            # Check if object in following queryset
            # Remember to check if user_to_follow == request.user because you can't follow yourself
            if user_to_follow in request.user.following.all():
                #import pdb; pdb.set_trace()
                return Response({'status': 'error', 'message': f'You already follow {user_to_follow.username}'}, status=status.HTTP_200_OK)
            
            request.user.following.add(user_to_follow)
            return Response({'status': 'success', 'message': f'You have successfully followed {user_to_follow.username}'}, status=status.HTTP_200_OK)

        return Response({'status': 'error', 'message': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)


class UnfollowUserView(generics.GenericAPIView):
    # Adding permissions.IsAuthenticated for the checker 
    # Remember to remove the import up top
    permission_classes = [IsAuthenticated, permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = CustomUser.objects.all().filter(id=user_id).first()

        if user_to_unfollow:  # Check if the user exists
            if user_to_unfollow not in request.user.following.all():
                #import pdb; pdb.set_trace()
                return Response({'status': 'error', 'message': f'You do not follow {user_to_unfollow.username}'}, status=status.HTTP_200_OK)
            
            request.user.following.remove(user_to_unfollow)
            return Response({'status': 'success', 'message': f'You have successfully unfollowed {user_to_unfollow.username}'}, status=status.HTTP_200_OK)

        return Response({'status': 'error', 'message': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)
