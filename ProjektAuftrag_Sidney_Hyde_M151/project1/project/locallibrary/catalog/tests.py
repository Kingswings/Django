from django.test import TestCase
from django.urls import reverse
from catalog.models import Book, Author

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

class BookModelTest(TestCase):
    def test_book_model_string_representation(self):
        book = Book(title='Test Book')
        self.assertEqual(str(book), 'Test Book')

class AuthorModelTest(TestCase):
    def test_author_model_string_representation(self):
        author = Author(first_name='John', last_name='Doe')
        self.assertEqual(str(author), 'Doe, John')
