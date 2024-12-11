from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

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


# posts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer  # Ensure you import your serializer

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # Get the list of users the current user is following
        following_users = user.following.all()

        # Fetch the posts by users the current user is following
        posts = Post.objects.filter(author__in=following_users).order_by('-published_date')

        # Serialize the posts
        serialized_posts = PostSerializer(posts, many=True).data

        # Return the serialized data
        return Response(serialized_posts, status=status.HTTP_200_OK)


from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification

@login_required
def like_post(request, post_id):
    """Handles liking a post."""
    post = get_object_or_404(Post, id=post_id)

    # Check if the user has already liked the post
    if Like.objects.filter(user=request.user, post=post).exists():
        return JsonResponse({'message': 'You have already liked this post.'}, status=400)

    # Create a new Like entry
    Like.objects.create(user=request.user, post=post)

    # Create a notification for the like action
    Notification.objects.create(
        recipient=post.author,  # The post's author gets notified
        actor=request.user,  # The user who liked the post
        verb="liked your post",  # Description of the action
        target=post,  # The target object (the post)
    )

    return JsonResponse({'message': 'Post liked successfully.'}, status=200)

@login_required
def unlike_post(request, post_id):
    """Handles unliking a post."""
    post = get_object_or_404(Post, id=post_id)

    # Check if the user has liked the post
    like = Like.objects.filter(user=request.user, post=post).first()
    if not like:
        return JsonResponse({'message': 'You have not liked this post.'}, status=400)

    # Delete the Like entry
    like.delete()

    # Optionally create a notification for the unlike action (if needed)
    Notification.objects.create(
        recipient=post.author,  # The post's author gets notified
        actor=request.user,  # The user who unliked the post
        verb="unliked your post",  # Description of the action
        target=post,  # The target object (the post)
    )

    return JsonResponse({'message': 'Post unliked successfully.'}, status=200)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LikeSerializer
from .models import Post

@api_view(['POST'])
def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user has already liked the post
    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create a like instance
    like = Like.objects.create(user=request.user, post=post)

    # Serialize the like data
    serializer = LikeSerializer(like)
    
    return Response(serializer.data, status=status.HTTP_201_CREATED)
