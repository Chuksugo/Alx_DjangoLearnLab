from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

# Registration View
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log in the user
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

# Logout View
def logout_view(request):
    logout(request)  # Log out the user
    return redirect('login')

# Profile View
@login_required(login_url='/login/')  # Ensure the user is logged in
def profile(request):
    if request.method == "POST":
        user = request.user
        # Update the user's email if provided
        user.email = request.POST.get("email", user.email)
        user.save()
        messages.success(request, "Profile updated successfully.")
        return redirect('profile')  # Redirect to the profile page
    return render(request, "blog/profile.html")



from django.shortcuts import render

@login_required 
def home(request):
    """
    View for the home page.
    """
    return render(request, "blog/home.html")



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# ListView for displaying all posts
class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'posts'

# DetailView for displaying a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

# CreateView for creating a new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# UpdateView for editing a post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# DeleteView for deleting a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm

# View to add a comment to a post
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('post_detail', pk=self.kwargs['post_id'])

# View to edit a comment
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_form.html'

    def get_success_url(self):
        return redirect('post_detail', pk=self.object.post.pk)

# View to delete a comment
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_confirm_delete.html'

    def get_success_url(self):
        return redirect('post_detail', pk=self.object.post.pk)



# View for updating an existing comment
def comment_update(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)  # Redirect to the post's detail page
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comment_update.html', {'form': form})

# View for creating a new comment for a specific post
def new_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)  # Redirect to the post's detail page
    else:
        form = CommentForm()
    return render(request, 'new_comment.html', {'form': form, 'post': post})



from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search_view(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()
    
    return render(request, 'search_results.html', {'posts': posts, 'query': query})


def tag_view(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(request, 'tagged_posts.html', {'posts': posts, 'tag': tag})


from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .models import Post, Tag

class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        tag_slug = self.kwargs.get('tag_slug')
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags=tag)
