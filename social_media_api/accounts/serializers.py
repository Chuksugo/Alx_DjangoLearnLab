from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser  # Ensure this import is correct

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser  # Ensure CustomUser is imported
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    """
    class Meta:
        model = get_user_model()  # Ensures compatibility with the custom user model
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create the user using the custom user model's manager
        user = get_user_model().objects.create_user(**validated_data)

        # Create a token for the new user
        Token.objects.create(user=user)

        return user

class LoginSerializer(serializers.Serializer):
    """
    Serializer for handling user login, including authentication validation.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Authenticate the user
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid credentials')

        # Generate or retrieve the token
        token, created = Token.objects.get_or_create(user=user)

        return {
            'user': user,
            'token': token.key  # Return the token key
        }
