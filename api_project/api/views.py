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

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book records
    serializer_class = BookSerializer  # Specify the serializer to use
