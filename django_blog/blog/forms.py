from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag
from .models import Comment

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    # Ensure the indentation here is consistent with the rest of the class
    def clean_tags(self):
        tags = self.cleaned_data['tags']
        # Add any additional logic you need for tag validation
        return tags



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

