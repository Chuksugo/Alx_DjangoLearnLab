# relationship_app/urls.py

from django.urls import path
from .views import list_books, LibraryDetailView  # Importing the views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Route to function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Route to class-based view
]




# relationship_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),  # Assuming you have a register_view in views.py
]


from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]

# LibraryProject/relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),  # Add Book URL
    path('edit_book/<int:id>/', views.edit_book, name='edit_book'),  # Edit Book URL
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),  # Delete Book URL
]
