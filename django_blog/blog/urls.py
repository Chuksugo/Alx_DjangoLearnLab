from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),  # Corrected to match view name
    path('', views.home, name='home'),  # Home page route
]
