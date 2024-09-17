from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Author, Book
from django.contrib.auth.models import User
import json

class BookAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.test_author = Author.objects.create(
                name="Test Author"
            )

        # Only logged in user can create a book.
        # self.test_book = Book.objects.create(
        #     title='Test Book',
        #     author = self.test_author,
        #     publication_year='2023-05-01'
        # )

        self.test_user = User.objects.create_user(username='test_user', password='testpassword')


    def test_book_list_GET(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)

    def test_create_book_not_logged_in(self):
        response = self.client.post(reverse('new_book'), {
            'title': 'Test Book 2',
            'author': self.test_author.pk,
            'publication_year': '2023-05-01'
        })
        self.assertEqual(response.status_code, 403)

    def test_user_is_able_to_login(self):
        response = self.client.login(username='test_user', password='testpassword')
        self.assertEqual(response, True)
        self.client.logout

    # Getting a 403 error with this. To be fixed
    def test_create_book_user_logged_in(self):
        self.client.login(username='test_user', password='testpassword')

        # Create Book
        book_data = {
            'title': 'Test Book',
            'author': self.test_author.pk,
            'publication_year': '2023-05-01'
        }
        response = self.client.post(reverse('new_book'), book_data)
        self.assertEqual(response.status_code, 201)
        created_book = Book.objects.get(title=book_data['title'])
        self.assertEqual(created_book.author, self.test_author)