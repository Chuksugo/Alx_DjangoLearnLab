# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView  # Importing the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route to function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route to class-based view
]




# relationship_app/urls.py

from django.urls import path
from .views import register  # Import the register view
from django.contrib.auth.views import LoginView, LogoutView  # Import LoginView and LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login view with custom template
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout view with custom template
    path('register/', register, name='register'),  # Registration view (custom register view)
]


