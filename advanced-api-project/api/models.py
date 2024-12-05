from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author Name")

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Book Title")
    publication_year = models.IntegerField(verbose_name="Publication Year")
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# The Author model represents the creators of books. Each author can have multiple books associated with them.
# The Book model represents individual books with a title, publication year, and a reference to the author.
