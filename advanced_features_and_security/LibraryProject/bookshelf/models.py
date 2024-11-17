from django.db import models
from django.conf import settings  # Import settings to reference the custom user model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Reference the custom user model
        on_delete=models.CASCADE,
        related_name='books'  # Optional: allows reverse lookup like user.books.all()
    )

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


        


from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)



from django.db import models  # Import the models module to define model fields

class Book(models.Model):
    title = models.CharField(max_length=200)  # A character field for the book title
    author = models.CharField(max_length=100)  # A character field for the author's name
    publication_date = models.DateField()  # A date field for the publication date

    @property
    def publication_year(self):
        """Return the year of publication from the publication_date."""
        return self.publication_date.year

    def __str__(self):
        """Return the book title as the string representation of the object."""
        return self.title



# bookshelf/models.py
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser with an email, username, and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()  # Use the custom user manager

    def __str__(self):
        return self.username
