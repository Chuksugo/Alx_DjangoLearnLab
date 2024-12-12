from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# posts/urls.py
from django.urls import path
from .views import FeedView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
]


# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:pk>/like/', views.LikePostView.as_view(), name='like_post'),
    path('posts/<int:pk>/unlike/', views.UnLikePostView.as_view(), name='unlike_post'),
]
