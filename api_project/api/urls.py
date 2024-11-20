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



from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet  # Import your BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')  # Register the BookViewSet

urlpatterns = [
    path('', include(router.urls)),  # Include the router-generated URLs
]
