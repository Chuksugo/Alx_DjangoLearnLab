from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


from rest_framework import serializers
from .models import Like
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Like
        fields = ['user', 'post']

    def validate(self, data):
        """Ensure a user can't like the same post twice."""
        user = data['user']
        post = data['post']

        if Like.objects.filter(user=user, post=post).exists():
            raise serializers.ValidationError("You have already liked this post.")
        
        return data

    def create(self, validated_data):
        """Create a like instance and return it."""
        return Like.objects.create(**validated_data)
