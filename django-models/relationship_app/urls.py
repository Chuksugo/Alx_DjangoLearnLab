# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView  # Importing the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route to function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route to class-based view
]



# relationship_app/urls.py

from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Login view
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout view
    path('register/', register, name='register'),  # Registration view
]

