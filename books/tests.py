# The python standard testing framework is unittest that uses TestCase
# TestCase is used when we want to test the database
from django.test import TestCase
# reverse confirms the named URL used
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    # Fill dummy information as a book
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title = "A good Title",
            subtitle = "The subtitle must be good",
            author = "Dubois",
            isbn = "1234567890987",
        )
    # AssertEqaul ensures that the book data entered is equal to the book content. 
    # Tests that first and second are equal. If the values do not compare equal, the test will fail.
    def test_book_content(self):
        self.assertEqual(self.book.title, "A good Title")
        self.assertEqual(self.book.subtitle, "The subtitle must be good")
        self.assertEqual(self.book.author, "Dubois")
        self.assertEqual(self.book.isbn, "1234567890987")
        
    # This test checks the response uses the named URL "home", returns a HTTP Response status of 200, contains expected text and uses the template books/booK_list.html
    def test_book_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        # "assertContains" is used specifically for responses and asserts that a response produced the given status_code and that text appears in its content.
        self.assertContains(response, "The subtitle must be good")
        # "assertTemplateUsed" asserts that the template with the given name was used in rendering the response.
        self.assertTemplateUsed(response, "books/book_list.html")