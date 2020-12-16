from django.db import models
from users.models import User
class Record(models.Model):
    audio = models.FileField()
    uid = models.ForeignKey('users.User',on_delete=models.CASCADE)
