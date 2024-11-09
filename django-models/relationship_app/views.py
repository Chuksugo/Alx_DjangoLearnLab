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
