from django.contrib import admin

from .models import CustomerOrSupplier


# Register your models here.
@admin.register(CustomerOrSupplier)
class CustomerOrSupplierAdmin(admin.ModelAdmin):
    list_display_links = ("company_name",)
    list_display = (
        "company_name",
        "nit_or_rut",
        "email",
        "is_customer",
        "is_supplier",
        "is_active",
        "date",
    )
    list_filter = (
        "company_name",
        "nit_or_rut",
        "email",
    )
    list_editable = (
        "is_customer",
        "is_supplier",
        "is_active",
    )
    ordering = ("-date",)
