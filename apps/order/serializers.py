from rest_framework import serializers
from django.utils import timezone
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    orderNumber = serializers.CharField(source="order_number", required=False)
    customer = serializers.CharField(source="customer_name", required=False, allow_blank=True, allow_null=True)
    channel = serializers.CharField(source="customer_type", required=False, allow_blank=True, allow_null=True)
    total = serializers.DecimalField(source="total_amount", max_digits=12, decimal_places=2, required=False)
    date = serializers.DateField(source="order_date", required=False)
    companyName = serializers.CharField(source="company_name", required=False, allow_blank=True, allow_null=True)
    personName = serializers.CharField(source="contact_person", required=False, allow_blank=True, allow_null=True)
    contactNo = serializers.CharField(source="phone", required=False, allow_blank=True, allow_null=True)
    vatNumber = serializers.CharField(source="vat", required=False, allow_blank=True, allow_null=True)
    panNumber = serializers.CharField(source="pan", required=False, allow_blank=True, allow_null=True)
    items = serializers.ListField(child=serializers.DictField(), required=False, write_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "orderNumber",
            "customer",
            "channel",
            "companyName",
            "personName",
            "email",
            "contactNo",
            "vatNumber",
            "panNumber",
            "address",
            "total",
            "date",
            "items",
            "expected_delivery",
            "status",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        return attrs

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if not data.get("channel"):
            data["channel"] = "physical"
        return data

    def create(self, validated_data):
        validated_data.pop("items", None)
        if not validated_data.get("order_number"):
            count = Order.objects.count() + 1
            validated_data["order_number"] = f"ORD-{timezone.now().year}-{count:04d}"
        if not validated_data.get("order_date"):
            validated_data["order_date"] = timezone.now().date()
        if not validated_data.get("total_amount"):
            validated_data["total_amount"] = 0
        return super().create(validated_data)
