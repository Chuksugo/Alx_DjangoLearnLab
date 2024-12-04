from django.urls import path
from . import views  # Import views from the same app
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),  # Corrected to match view name
    path('', views.home, name='home'),  # Home page route
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),  # Add this line for updating posts
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
]


from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView, PostByTagListView
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_id>/comments/new/', CommentCreateView.as_view(), name='comment_new'),  # Path for creating a comment
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),  # Path for editing a comment
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update/', views.comment_update, name='comment_update'),
    path('post/<int:pk>/comments/new/', views.new_comment, name='new_comment'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),
]

from django.urls import path
from .views import search_view, tag_view

urlpatterns = [
    path('search/', search_view, name='search'),
    path('tags/<str:tag_name>/', tag_view, name='tagged_posts'),
]
