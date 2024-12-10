# accounts/views.py
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    """
    API view for registering a new user.
    """
    queryset = User.objects.all()
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
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            return Response({'error': 'Invalid credentials'}, status=400)
        return Response(serializer.errors, status=400)

class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = User.objects.get(id=user_id)
            if request.user == user_to_follow:
                return Response({"error": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)
            if user_to_follow in request.user.following.all():
                return Response({"error": "You are already following this user"}, status=status.HTTP_400_BAD_REQUEST)
            
            request.user.following.add(user_to_follow)
            return Response({"message": "Followed successfully!"}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            if user_to_unfollow not in request.user.following.all():
                return Response({"error": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)
            
            request.user.following.remove(user_to_unfollow)
            return Response({"message": "Unfollowed successfully!"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
