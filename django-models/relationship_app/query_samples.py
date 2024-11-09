from relationship_app.models import Author, Book, Library, Librarian

# Query all books in the database using books.all()
def get_all_books():
    books = Book.objects.all()  # Retrieving all books
    return books

# Query all books by a specific author using objects.filter
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # Filtering books by author
    return books

# List all books in a library using objects.filter
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = Book.objects.filter(libraries=library)  # Filtering books by library (ManyToMany relationship)
    return books

# Retrieve the librarian for a library using objects.get
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)  # Getting librarian by library instance
        return librarian
    except Library.DoesNotExist:
        return None  # Library not found
    except Librarian.DoesNotExist:
        return None  # Librarian not found for this library
