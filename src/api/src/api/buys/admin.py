from django.contrib import admin

from .models import Buy


# Register your models here.
@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "acount",
        "unit_cost",
        "supplier",
        "date",
    )
    list_display_links = ("product",)
    list_filter = (
        "supplier",
        "date",
    )
    search_fields = (
        "product",
        "supplier",
        "date",
    )
    ordering = ("-date",)
