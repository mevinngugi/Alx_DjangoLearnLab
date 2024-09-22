from django.shortcuts import render
from .models import CustomUser
from .serializers import CustomUserSerializer, LoginUserSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate


# Create your views here.
class RegisterCustomUserView(generics.CreateAPIView):
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
