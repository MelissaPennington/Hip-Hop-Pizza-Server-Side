from django.db import models
from .user import User


class Order(models.Model):

    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    timestamp = models.DateTimeField()
    payment_type = models.CharField(max_length=50)
    order_type = models.CharField(max_length=50)
    tip_amount = models.IntegerField()
    total = models.DecimalField(max_digits=7, decimal_places=2)
    is_open = models.BooleanField(null=True, blank=True)
