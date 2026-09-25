from django.shortcuts import render

from .models import CustomerOrSupplier


# Create your views here.
def customer_list(request: None):
    customer = CustomerOrSupplier.objects.filter(is_customer=True, is_active=True)
    return render(request, "", {"customer": customer})
