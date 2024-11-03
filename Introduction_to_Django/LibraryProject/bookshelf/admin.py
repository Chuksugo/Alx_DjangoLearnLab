from django.contrib import admin
from .models import Book

# Custom admin class to manage Book model display and functionality
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields displayed in the list view
    search_fields = ('title', 'author__name')  # Enable searching by title and author's name
    list_filter = ('publication_year',)  # Add filter for publication year

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
