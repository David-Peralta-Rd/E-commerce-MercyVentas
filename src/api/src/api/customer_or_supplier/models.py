from django.db import models


# Create your models here.
class CustomerOrSupplier(models.Model):
    company_name = models.CharField(max_length=255)
    nit_or_rut = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    # Flags
    is_customer = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)

    # State
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name
