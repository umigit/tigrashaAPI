from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Post(models.Model):
    title = models.CharField(max_length=16)
    name = models.CharField(max_length=32)
    place = models.CharField(max_length=32)
    date = models.CharField(max_length=32)
    detail = models.TextField(default="")
    address = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='image/%Y%m%d')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)
