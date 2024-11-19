# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # The model query to retrieve all books
    serializer_class = BookSerializer  # The serializer to format the data
