from django.db import models
from users.models import User
from books.models import Book

class Record(models.Model):
    audio = models.FileField()
    book = models.ForeignKey('books.Book',on_delete=models.CASCADE)
    reader = models.ForeignKey('users.User', db_column="users_id", on_delete=models.CASCADE)
