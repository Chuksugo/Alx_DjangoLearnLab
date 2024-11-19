from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router instance
router = DefaultRouter()

# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

# Include the router URLs
urlpatterns = [
    # Remove the BookList route because you now have the BookViewSet handling CRUD
    path('', include(router.urls)),  # This will include all CRUD routes for the Book model
]
