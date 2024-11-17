from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        # Logic for creating a new book
        pass
    return render(request, 'create_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        # Logic for editing the book
        pass
    return render(request, 'edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        # Logic for deleting the book
        book.delete()
    return render(request, 'delete_book.html', {'book': book})

    

from django.shortcuts import render
from .models import Book

# View to display a list of all books
def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'book_list.html', {'books': books})


def book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Process the valid data
            pass