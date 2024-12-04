from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment
from taggit.forms import TagWidget

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    # Custom widget for the title field
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter post title', 'class': 'custom-class'})
    )




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

