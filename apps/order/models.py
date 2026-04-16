from django.db import models
from apps.core.models import BaseModel


class Order(BaseModel):
    order_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_type = models.CharField(
        max_length=50,
        choices=[("company", "Company"), ("individual", "Individual")],
        blank=True,
        null=True,
    )
    company_name = models.CharField(max_length=255, blank=True, null=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    vat = models.CharField(max_length=50, blank=True, null=True)
    pan = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    order_date = models.DateField()
    expected_delivery = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("processing", "Processing"),
            ("delivered", "Delivered"),
            ("completed", "Completed"),
        ],
        default="pending",
    )
    record_status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("deleted", "Deleted")],
        default="active",
    )

    class Meta:
        db_table = "order"

    def __str__(self):
        return f"Order {self.order_number}"
