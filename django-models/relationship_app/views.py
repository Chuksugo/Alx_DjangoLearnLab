from django.shortcuts import render
from django.apps import apps

def list_books_in_library(request, library_name):
    # Load Library model dynamically
    Library = apps.get_model('relationship_app', 'Library')
    Book = apps.get_model('relationship_app', 'Book')
    
    library = Library.objects.filter(name=library_name).first()
    books = Book.objects.filter(libraries=library) if library else []
    return render(request, 'relationship_app/book_list.html', {'library': library, 'books': books})

def get_librarian_for_library(request, library_name):
    Library = apps.get_model('relationship_app', 'Library')
    Librarian = apps.get_model('relationship_app', 'Librarian')
    
    library = Library.objects.filter(name=library_name).first()
    librarian = Librarian.objects.filter(library=library).first() if library else None
    return render(request, 'relationship_app/librarian_detail.html', {'library': library, 'librarian': librarian})
