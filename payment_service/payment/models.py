from __future__ import unicode_literals
from django.db import models


# Create your models here.
class payment_status(models.Model):
    ### The following are the fields of our table.
    username = models.CharField(max_length=50)
    order_id = models.IntegerField(default=1)
    status = models.CharField(max_length=15)


    def __str__(self):
        return '%s %s %s %s %s %s %s ' % (self.username, self.order_id, self.status)
    

