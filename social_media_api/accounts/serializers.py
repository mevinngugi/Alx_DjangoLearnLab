from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Initial implementation of CustomUserSerializer

# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         # Because we are extending Abstract User class in the model,
#         # we have access to things like username and password 
#         fields = ['email', 'username', 'password', 'bio', 'profile_picture']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

#     # Pass in validation for the custom user 
#     def validate(self, data):
#         #import pdb; pdb.set_trace()
#         if len(data['username']) < 3:
#             raise serializers.ValidationError({
#                 'username': 'Username too short'})
#         return data

#     def create(self, validated_data):
#         return CustomUser.objects.create_user(**validated_data)


class CustomUserSerializer(serializers.ModelSerializer):
    # Sample validation using CharField
    username = serializers.CharField(min_length=3, allow_blank=False)
    bio = serializers.CharField(max_length=500, allow_blank=True)
    # Sets the email field to be required and can not be blank
    email = serializers.EmailField(allow_blank=False)

    class Meta:
        model = CustomUser
        # Because we are extending Abstract User class in the model,
        # we have access to things like username and password 
        fields = ['email', 'username', 'password', 'bio', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Pass in validation for the custom user 
    def validate(self, data):
        #import pdb; pdb.set_trace()
        filter_for_existing_username = CustomUser.objects.filter(username=data['username']).exists()
        if filter_for_existing_username:
            raise serializers.ValidationError({'username': 'Username must be unique.'})

        filter_for_existing_email = CustomUser.objects.filter(email=data['email']).exists()
        if filter_for_existing_email:
            raise serializers.ValidationError({'email': 'Email must be unique.'})
            
        return data

    def create(self, validated_data):
        # get_user_model() returns the current active user model. User otherwise
        user = get_user_model().objects.create_user(**validated_data)
        # Create token every time a new user is created.
        # Moved here from post signal in model.
        Token.objects.create(user=user)
        return user

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(allow_blank=False)
    password = serializers.CharField(allow_blank=False)

