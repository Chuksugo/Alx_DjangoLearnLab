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

def home(request):
    """
    View for the home page.
    """
    return render(request, "blog/home.html")

