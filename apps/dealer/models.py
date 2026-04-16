from django.db import models
from apps.core.models import BaseModel


class Dealer(BaseModel):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    dealer_type = models.CharField(
        max_length=50,
        choices=[
            ("supplier", "Supplier"),
            ("buyer", "Buyer"),
            ("stakeholder", "Stakeholder"),
            ("other", "Other"),
        ],
        blank=True,
        null=True,
    )
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("inactive", "Inactive"), ("deleted", "Deleted")],
        default="active",
    )

    class Meta:
        db_table = "dealer"

    def __str__(self):
        return self.name
