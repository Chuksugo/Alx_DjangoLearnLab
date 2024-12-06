from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book  # Adjust the import as needed
from django.contrib.auth.models import User  # Or use a custom user model

class BookAPITests(TestCase):
    def setUp(self):
        # Create a test user and authenticate with APIClient
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.book_data = {
            'title': 'Test Book',
            'content': 'This is a test book.',
            'published_date': '2024-12-06',
            'author': self.user.id,
        }

    def test_create_book(self):
        response = self.client.post('/api/books/', self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_get_book(self):
        # First, create a book
        book = Book.objects.create(**self.book_data)
        response = self.client.get(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        book = Book.objects.create(**self.book_data)
        updated_data = {'title': 'Updated Test Book'}
        response = self.client.put(f'/api/books/{book.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Test Book')

    def test_delete_book(self):
        book = Book.objects.create(**self.book_data)
        response = self.client.delete(f'/api/books/{book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=book.id).exists())

    def test_permission_restriction(self):
        # Create a book as a different user
        other_user = User.objects.create_user(username='otheruser', password='otherpassword')
        self.client.force_authenticate(user=other_user)
        response = self.client.get(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_books(self):
        Book.objects.create(title='Old Book', published_date='2023-01-01', author=self.user)
        Book.objects.create(title='New Book', published_date='2024-12-06', author=self.user)
        response = self.client.get('/api/books/?published_date=2024-12-06')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_books(self):
        Book.objects.create(title='First Book', published_date='2023-01-01', author=self.user)
        Book.objects.create(title='Second Book', published_date='2024-12-06', author=self.user)
        response = self.client.get('/api/books/?ordering=published_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'First Book')
