from django.db import models

class User(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=100)
    account = models.TextField()
