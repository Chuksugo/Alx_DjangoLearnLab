# relationship_app/views.py

from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all book records
    return render(request, 'relationship_app/list_books.html', {'books': books})

# relationship_app/views.py

from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library  # Specify the model to use
    template_name = 'relationship_app/library_detail.html'  # Specify the template to render
    context_object_name = 'library'  # Name of the context variable for the library object





# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change 'home' to the URL name where you want to redirect after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

