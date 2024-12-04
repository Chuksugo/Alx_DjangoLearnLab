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



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']



class TagWidget(forms.TextInput):  # Define a simple custom widget for tags
    def __init__(self, attrs=None):
        default_attrs = {'placeholder': 'Add tags separated by commas'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(attrs=default_attrs)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # Assign the custom widget to the tags field
        }
