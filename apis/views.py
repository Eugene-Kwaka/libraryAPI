from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from .serializers import BookSerializer

# Create your views here.
# ListAPIView is used for read-only endpoints to represent a collection of model instances
class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer