from django.db import models
from users.models import User

class Book(models.Model):
    cover = models.ImageField()
    title = models.TextField()
    author = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    reader = models.ForeignKey(User, default='-', on_delete=models.CASCADE)