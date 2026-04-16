from rest_framework import serializers
from .models import Transaction, TransactionType, IncomeCategory, ExpenseCategory


class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = ["id", "name", "description", "icon", "created_at", "updated_at"]


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ["id", "name", "transaction_type", "description", "created_at", "updated_at"]


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ["id", "name", "transaction_type", "description", "created_at", "updated_at"]


class TransactionSerializer(serializers.ModelSerializer):
    source = serializers.CharField(required=False, allow_blank=True, allow_null=True, write_only=True)

    class Meta:
        model = Transaction
        fields = [
            "id",
            "type",
            "category",
            "amount",
            "description",
            "date",
            "reference",
            "source",
            "status",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        validated_data.pop("source", None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop("source", None)
        return super().update(instance, validated_data)
