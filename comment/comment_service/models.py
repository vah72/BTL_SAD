
from __future__ import unicode_literals
from django.db import models
class product_comment(models.Model):
    comment = models.TextField()
    rating = models.IntegerField() #one to five star
    uname = models.CharField(max_length=250)
    product_id = models.CharField(max_length=250)
    # orderitem_id = models.IntegerField()