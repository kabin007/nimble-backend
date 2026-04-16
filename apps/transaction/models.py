from django.db import models
from apps.core.models import BaseModel


class TransactionType(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = "transaction_type"

    def __str__(self):
        return self.name


class IncomeCategory(BaseModel):
    name = models.CharField(max_length=255)
    transaction_type = models.ForeignKey(
        TransactionType, on_delete=models.CASCADE, related_name="income_categories"
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "income_category"

    def __str__(self):
        return self.name


class ExpenseCategory(BaseModel):
    name = models.CharField(max_length=255)
    transaction_type = models.ForeignKey(
        TransactionType, on_delete=models.CASCADE, related_name="expense_categories"
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "expense_category"

    def __str__(self):
        return self.name


class Transaction(BaseModel):
    type = models.CharField(max_length=100)
    category = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    reference = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("deleted", "Deleted")],
        default="active",
    )

    class Meta:
        db_table = "transaction"

    def __str__(self):
        return f"{self.type} - {self.amount}"