from rest_framework import serializers
from .models import Notification
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    recipient = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    target = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), required=False)

    class Meta:
        model = Notification
        fields = ['actor', 'recipient', 'verb', 'target', 'timestamp']
        read_only_fields = ['timestamp']

    def create(self, validated_data):
        """Create and return a notification instance."""
        return Notification.objects.create(**validated_data)
