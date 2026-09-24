from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    cost = models.DecimalField(max_digits=25, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
