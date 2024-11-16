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
