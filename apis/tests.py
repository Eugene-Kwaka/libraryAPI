from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
# Create your tests here.

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "Django for APIs",
            subtitle = "Build Web APIs using Django Rest Framework",
            author = "Eugene",
            isbn = "1234567891012"
        )
        
    def test_api_list_view(self):
        # Get the correct URL based on the URL name given
        response = self.client.get(reverse("book_list"))
        # Assert that the HTTP Status provided is 200
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that there is a single entry in the database according to the setUpTestData (1 book has been created)
        self.assertEqual(Book.objects.count(), 1)
        # Assert that the response contains the data(content) from the created book object
        self.assertContains(response, self.book)
