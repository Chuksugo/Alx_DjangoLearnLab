from django.contrib import admin
from django.urls import path, include  # Include 'include' to link app-level URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # Delegate all blog-related routes to blog/urls.py
]
