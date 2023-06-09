from django.db import models

# Create your models here.
class Image(models.Model):
    url = models.CharField(max_length=200)
    product_id=models.IntegerField()
    description=models.CharField(max_length=200)