from django.contrib import admin

from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display_links = ("name",)
    list_display = (
        "name",
        "price",
        "cost",
        "stock",
        "date",
    )
    list_filter = (
        "name",
        "stock",
    )
    list_editable = (
        "stock",
        "price",
        "cost",
    )
    ordering = ("-date",)
