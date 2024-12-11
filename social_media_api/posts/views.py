from rest_framework import viewsets, permissions, filters
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import LikeSerializer
from rest_framework.decorators import api_view
from notifications.models import Notification
from django.http import JsonResponse

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

# Like and Unlike Post functionality
@api_view(['POST'])
def like_post(request, post_id):
    # Fetch post using get_object_or_404
    post = get_object_or_404(Post, id=post_id)

    # Check if the user has already liked the post
    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

    # Create a like instance
    like = Like.objects.create(user=request.user, post=post)
    serializer = LikeSerializer(like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# In posts/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def unlike_post(request, post_id):
    # Get the post object or return 404 if not found
    post = get_object_or_404(Post, pk=post_id)

    # Try to get the like object if it exists
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()  # Remove the like
    except Like.DoesNotExist:
        return JsonResponse({'message': 'You have not liked this post yet.'}, status=400)

    # Create a notification for the unliked action
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='unliked your post',
        target=post
    )

    return JsonResponse({'message': 'Post unliked successfully.'}, status=200)


# PostDetailView to get details of a specific post
class PostDetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
