from django.db import models

# Create your models here.
class Clothe (models.Model):
    name = models.CharField(max_length=200)
    brand=models.CharField(max_length=200)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)
    