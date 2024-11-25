from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer to format the response


from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import the corresponding serializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  # Query all books
    serializer_class = BookSerializer  # Use the Book serializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access

from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the serializer to serialize data
