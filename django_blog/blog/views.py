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
