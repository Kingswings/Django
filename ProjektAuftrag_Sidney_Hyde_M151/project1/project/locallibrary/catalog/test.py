from django.test import TestCase
from django.urls import reverse
from datetime import date
from datetime import timedelta
from django.contrib.auth.models import User
from .models import Genre, Book, BookInstance, Author

class GenreModelTest(TestCase):

    def setUp(self):
        self.genre = Genre.objects.create(name='Science Fiction')

    def test_str_representation(self):
        self.assertEqual(str(self.genre), 'Science Fiction')

class BookModelTest(TestCase):

    def setUp(self):
        self.genre1 = Genre.objects.create(name='Science Fiction')
        self.genre2 = Genre.objects.create(name='Fantasy')
        self.author = Author.objects.create(first_name='John', last_name='Doe')
        self.book = Book.objects.create(
            title='Book Title',
            author=self.author,
            summary='Book summary',
            isbn='1234567890123'
        )
        self.book.genre.set([self.genre1, self.genre2])

    def test_str_representation(self):
        self.assertEqual(str(self.book), 'Book Title')

    def test_get_absolute_url(self):
        expected_url = reverse('book-detail', args=[str(self.book.id)])
        self.assertEqual(self.book.get_absolute_url(), expected_url)

    def test_display_genre(self):
        expected_genre = 'Science Fiction, Fantasy'
        self.assertEqual(self.book.display_genre(), expected_genre)

class BookInstanceModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name='John', last_name='Doe')
        self.book = Book.objects.create(
            title='Book Title',
            author=self.author,
            summary='Book summary',
            isbn='1234567890123'
        )
        self.book_instance = BookInstance.objects.create(
            book=self.book,
            imprint='Imprint',
            due_back=date.today(),
            borrower=User.objects.create_user(username='testuser', password='testpassword'),
            status='o'
        )

    def test_str_representation(self):
        expected_str = f'{self.book_instance.id} ({self.book.title})'
        self.assertEqual(str(self.book_instance), expected_str)

    def test_is_overdue(self):
        self.assertFalse(self.book_instance.is_overdue)

        self.book_instance.due_back = date.today() - timedelta(days=7)
        self.assertTrue(self.book_instance.is_overdue)

class AuthorModelTest(TestCase):

    def setUp(self):
        self.author = Author.objects.create(first_name='John', last_name='Doe')

    def test_str_representation(self):
        self.assertEqual(str(self.author), 'Doe, John')

    def test_get_absolute_url(self):
        expected_url = reverse('author-detail', args=[str(self.author.id)])
        self.assertEqual(self.author.get_absolute_url(), expected_url)
