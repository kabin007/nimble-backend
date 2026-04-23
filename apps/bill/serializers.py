from apps.dealer.models import Dealer
from rest_framework import serializers
from django.utils import timezone
from .models import Bill


class BillSerializer(serializers.ModelSerializer):
    vendor = serializers.PrimaryKeyRelatedField(
                                queryset=Dealer.objects.all()
                                )
    dueDate = serializers.DateField(source="due_date", required=False, allow_null=True)
    date = serializers.DateField(source="bill_date", required=False)
    billImage = serializers.CharField(source="bill_image", required=False, allow_blank=True, allow_null=True)
    billNumber = serializers.SerializerMethodField(read_only=True)
    items = serializers.ListField(child=serializers.DictField(), required=False, write_only=True)
    transactionType = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Bill
        fields = [
            "id",
            "billNumber",
            "vendor",
            "amount",
            "description",
            "billImage",
            "transactionType",
            "date",
            "dueDate",
            "items",
            "status",
            "created_at",
            "updated_at",
        ]

    def get_billNumber(self, obj):
        return f"BILL-{obj.id:04d}" if obj.id else "BILL-NEW"

    def create(self, validated_data):
        validated_data.pop("items", None)
        if not validated_data.get("bill_date"):
            validated_data["bill_date"] = timezone.now().date()
        return super().create(validated_data)
    
    def get_transactionType(self, obj):
        if not obj.vendor:
            return None

        if obj.vendor.dealer_type == "supplier":
            return "expense"
        elif obj.vendor.dealer_type == "buyer":
            return "income"

        return "expense"
