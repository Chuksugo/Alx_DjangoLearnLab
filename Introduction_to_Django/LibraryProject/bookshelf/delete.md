# Delete

Command:
```python
from bookshelf.models import Book  # Import the Book model

retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")  # Fetch the book to delete

retrieved_book.delete() # Delete the book instance

Book.objects.all() # Confirm deletion by checking all books

Expected Outcome:
<QuerySet []>  