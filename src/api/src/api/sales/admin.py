from django.contrib import admin

from .models import Sale


# Register your models here.
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display_links = ("product",)
    list_display = (
        "product",
        "acount",
        "unit_price",
        "customer",
        "date",
    )
    list_filter = (
        "product",
        "acount",
        "customer",
    )
    list_editable = (
        "acount",
        "unit_price",
    )
    ordering = ("-date",)
