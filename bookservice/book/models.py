from django.db import models

# Create your models here.
class Book (models.Model):
    name = models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    