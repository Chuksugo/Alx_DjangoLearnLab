# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView  # Importing the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route to function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route to class-based view
]
