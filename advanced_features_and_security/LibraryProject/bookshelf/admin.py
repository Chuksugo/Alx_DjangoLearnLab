from django.contrib import admin
from .models import Book

# Custom admin class to manage Book model display and functionality
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields displayed in the list view
    search_fields = ('title', 'author__name')  # Enable searching by title and author's name
    list_filter = ('publication_date',)  # Add filter for publication year

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

