from django.db import models


# Create your models here.
class Buy(models.Model):
    product = models.CharField(max_length=25)
    acount = models.PositiveSmallIntegerField(default=0)
    unit_cost = models.PositiveIntegerField(default=0)
    supplier = models.CharField(max_length=25)
    date = models.DateTimeField(auto_now=True)
