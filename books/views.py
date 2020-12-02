from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializer import BookSerializer

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
