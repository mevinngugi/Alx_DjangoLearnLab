from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
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
        if len(data['username']) < 3:
            raise serializers.ValidationError({
                'username': 'Username too short'})
        return data

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)