from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, LoginSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class RegisterView(generics.CreateAPIView):
    """
    API view for registering a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Public access for user registration

class LoginView(APIView):
    """
    API view for user login, returning a token if credentials are valid.
    """
    permission_classes = [AllowAny]  # Public access for login

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            # Authenticate the user
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None:
                # Generate or get the token
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=400)

        return Response(serializer.errors, status=400)



# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            request.user.following.add(user_to_follow)
            return Response({"message": "Followed successfully!"}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            request.user.following.remove(user_to_unfollow)
            return Response({"message": "Unfollowed successfully!"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
