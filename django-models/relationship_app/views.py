from django.shortcuts import render
from django.apps import apps

# Using apps.get_model to load Library dynamically
Library = apps.get_model('relationship_app', 'Library')

def list_books_in_library(request, library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return render(request, 'relationship_app/book_list.html', {'library': library, 'books': books})

def get_librarian_for_library(request, library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return render(request, 'relationship_app/librarian_detail.html', {'library': library, 'librarian': librarian})
