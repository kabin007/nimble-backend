from django.db import models
from apps.core.models import BaseModel
from apps.transaction.models import Transaction
from apps.dealer.models import Dealer


class Bill(BaseModel):
    vendor = models.ForeignKey(Dealer, on_delete=models.PROTECT, related_name="bills", blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    bill_image = models.URLField(blank=True, null=True)
    bill_date = models.DateField()
    due_date = models.DateField(blank=True, null=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True, blank=True, related_name="bills")
    status = models.CharField(
        max_length=20,
        choices=[("paid", "Paid"), ("unpaid", "Unpaid"), ("overdue", "Overdue")],
        default="unpaid",
    )
    record_status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("deleted", "Deleted")],
        default="active",
    )

    class Meta:
        db_table = "bill"

    def __str__(self):
        return f"Bill {self.id} - {self.amount}"
