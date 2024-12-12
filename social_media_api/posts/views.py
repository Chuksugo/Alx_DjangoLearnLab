from rest_framework import viewsets, permissions, filters
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from notifications.models import Notification
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Post and Comment ViewSets for CRUD operations via REST framework
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Feed View for getting posts from followed users
class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-published_date')
        serialized_posts = PostSerializer(posts, many=True).data
        return Response(serialized_posts, status=status.HTTP_200_OK)


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        
        if not created:
            return Response({"message": "You have already liked this post."}, status=400)
        
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

        return Response({"message": "Post liked successfully."}, status=201)



class UnLikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Use generics.get_object_or_404 to fetch the post or return 404 if not found
        post = generics.get_object_or_404(Post, pk=pk)
        
        # Find the like entry for the current user
        like = Like.objects.filter(post=post, user=request.user).first()
        
        if not like:
            return Response({"message": "You haven't liked this post."}, status=400)

        # Delete the like
        like.delete()
        return Response({"message": "Like removed."}, status=200)

class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        # Fetch the Post object or raise a 404 if it doesn't exist
        return get_object_or_404(Post, pk=self.kwargs['pk'])