from django.db import models

class Order(models.Model):
    user_id = models.IntegerField(default=1)
    cart_id = models.IntegerField(default=1)
    total = models.FloatField(default=0.0)
    shipment_id = models.IntegerField(default=1)

