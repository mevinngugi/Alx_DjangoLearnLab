from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Author, Book
from django.contrib.auth.models import User, Permission
from rest_framework import status
#import json

class BookAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.test_author = Author.objects.create(
                name="Test Author"
            )

        self.test_user = User.objects.create_user(username='test_user', password='testpassword')

        self.test_book = Book.objects.create(
            title='Test Book',
            author=self.test_author,
            publication_year='2022-05-01 00:00:00'
        )


    def test_book_list(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_book_detail(self):
        response = self.client.get(reverse('book_detail', kwargs={'pk': self.test_book.pk}))
        #print("Response Content:", response.content)
        #response_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print("Response Content as json:", response_data)
        self.assertEqual(response.data['title'], self.test_book.title)

    def test_book_update_user_not_logged_in(self):
        response = self.client.put(
            reverse('update_book', kwargs={'pk': self.test_book.pk}), {
            'title': 'Test Book Updated Title',
            'author': self.test_author.id,
            'publication_year': '2023-05-01 00:00:00'     
            })

        #response_data = response.json()
        #print("Response Content as json:", response_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_book_update_user_logged_in_WITHOUT_perms(self):
        self.client.login(username = self.test_user.username, password = 'testpassword')

        response = self.client.put(
            reverse('update_book', kwargs={'pk': self.test_book.pk}), {
            'title': 'Test Book Updated Title',
            'author': self.test_author.id,
            'publication_year': '2023-05-01 00:00:00'     
            })

        #response_data = response.json()
        #print("Response Content:", response.content)
        #print("Response Content as json:", response_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_book_update_user_logged_in_with_perms(self):
        self.client.login(username = self.test_user.username, password = 'testpassword')
        
        # Get and assign perms to change/ update Book
        permissions = Permission.objects.get(codename='change_book')
        self.test_user.user_permissions.add(permissions)

        response = self.client.put(
            reverse('update_book',
            kwargs={'pk': self.test_book.pk}), {
            'title': 'Test Book Updated Title',
            'author': self.test_author.id,
            'publication_year': '2023-05-01 00:00:00'     
            })

        #response_data = response.json()
        #print("Response Content:", response.content)
        #print("Response Content as json:", response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book Updated Title')
        self.test_user.user_permissions.remove(permissions)
        #print("Response.data: ", response.data)

    def test_create_book_user_logged_in(self):
        self.client.login(username=self.test_user.username, password='testpassword')

        permissions = Permission.objects.get(codename='add_book')
        self.test_user.user_permissions.add(permissions)

        # Create Book
        response = self.client.post(reverse('new_book'), {
            'title': 'Test Book Created Round 2',
            'author': self.test_author.id,
            'publication_year': '2023-05-01 00:00:00'            
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #response_data = response.json()
        #print("Response Content:", response.content)
        #print("Response Content as json:", response_data)
        #print("Response.data: ", response.data)
        self.assertEqual(response.data['author'], self.test_author.id)
        self.assertEqual(response.data['title'], 'Test Book Created Round 2')

    def test_delete_book_user_logged_in_WITHOUT_perms(self):
        self.client.login(username=self.test_user.username, password='testpassword')

        response = self.client.delete(
            reverse('delete_book', kwargs={'pk': self.test_book.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_user_logged_in_with_perms(self):
        self.client.login(username=self.test_user.username, password='testpassword')

        permissions = Permission.objects.get(codename='delete_book')
        self.test_user.user_permissions.add(permissions)

        response = self.client.delete(
            reverse('delete_book', kwargs={'pk': self.test_book.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
