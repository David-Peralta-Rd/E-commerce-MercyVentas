from django.db import models


# Create your models here.
class Sale(models.Model):
    product = models.CharField(max_length=25)
    acount = models.PositiveSmallIntegerField(default=0)
    unit_price = models.PositiveIntegerField(default=0)
    customer = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now=True)
