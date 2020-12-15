from django.db import models

class User(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=100)
    account = models.TextField()
    password = models.IntegerField(default=0)

    def __str__(self):
        return self.name