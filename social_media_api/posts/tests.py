from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from posts.models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class LikeSystemTests(TestCase):

    def setUp(self):
        # Create two users with email
        self.user1 = User.objects.create_user(username='user1', email='user1@example.com', password='password123')
        self.user2 = User.objects.create_user(username='user2', email='user2@example.com', password='password123')
        
        # Create a post
        self.post = Post.objects.create(
            author=self.user2,
            title='Test Post',
            content='This is a test post'
        )

    def test_like_post(self):
        """Test that a user can like a post and generate a notification."""
        # Log in as user1
        self.client.login(username='user1', password='password123')

        # Send a like request
        url = reverse('like_post', kwargs={'post_id': self.post.id})
        response = self.client.post(url)

        # Check if Like was created
        self.assertEqual(Like.objects.count(), 1)
        like = Like.objects.first()
        self.assertEqual(like.user, self.user1)
        self.assertEqual(like.post, self.post)

        # Check if notification was created
        self.assertEqual(Notification.objects.count(), 1)
        notification = Notification.objects.first()
        self.assertEqual(notification.actor, self.user1)
        self.assertEqual(notification.recipient, self.user2)
        self.assertEqual(notification.verb, 'liked your post')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post liked successfully.')

    def test_prevent_multiple_likes(self):
        """Test that a user cannot like a post multiple times."""
        # Log in as user1
        self.client.login(username='user1', password='password123')

        # Like the post
        self.client.post(reverse('like_post', kwargs={'post_id': self.post.id}))

        # Try to like the post again
        response = self.client.post(reverse('like_post', kwargs={'post_id': self.post.id}))

        # Ensure only one Like exists
        self.assertEqual(Like.objects.count(), 1)
        self.assertEqual(response.status_code, 400)
        self.assertContains(response, 'You have already liked this post.')

    def test_unlike_post(self):
        """Test that a user can unlike a post."""
        # Log in as user1 and like the post
        self.client.login(username='user1', password='password123')
        self.client.post(reverse('like_post', kwargs={'post_id': self.post.id}))

        # Send an unlike request
        response = self.client.post(reverse('unlike_post', kwargs={'post_id': self.post.id}))

        # Check if Like was deleted
        self.assertEqual(Like.objects.count(), 0)

        # Check if notification was created for unliking
        self.assertEqual(Notification.objects.count(), 2)  # 1 like + 1 unlike notification
        notification = Notification.objects.last()
        self.assertEqual(notification.actor, self.user1)
        self.assertEqual(notification.recipient, self.user2)
        self.assertEqual(notification.verb, 'unliked your post')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post unliked successfully.')

    def test_view_notifications(self):
        """Test that notifications are correctly displayed for a user."""
        # Log in as user2 (who will receive notifications)
        self.client.login(username='user2', password='password123')

        # Generate a notification for user2
        Notification.objects.create(
            recipient=self.user2,
            actor=self.user1,
            verb="liked your post",
            target=self.post
        )

        # Visit the notifications page
        response = self.client.get(reverse('view_notifications'))

        # Check if notifications are displayed
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'liked your post')
        self.assertContains(response, self.user1.username)
        self.assertContains(response, self.post.title)
