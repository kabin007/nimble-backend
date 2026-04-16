from django.db import models
from apps.core.models import BaseModel


class Inventory(BaseModel):
    item_name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField(default=0)
    min_stock = models.IntegerField(default=10)
    unit = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ("fabric", "Fabric"),
            ("garment", "Garment"),
            ("accessory", "Accessory"),
            ("raw_material", "Raw Material"),
        ],
        default="raw_material",
    )
    supplier = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("inactive", "Inactive"), ("deleted", "Deleted")],
        default="active",
    )

    class Meta:
        db_table = "inventory"

    def __str__(self):
        return self.item_name
