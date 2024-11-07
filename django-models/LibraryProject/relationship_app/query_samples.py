# relationship_app/query_samples.py
from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    """Query all books by a specific author."""
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books

def list_books_in_library(library_name):
    """List all books in a library."""
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def get_librarian_for_library(library_name):
    """Retrieve the librarian for a library."""
    library = Library.objects.get(name=library_name)
    librarian = library.librarian  # Access the librarian through the OneToOne relationship
    return librarian
