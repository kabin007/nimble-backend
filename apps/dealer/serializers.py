from rest_framework import serializers
from .models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source="name")
    contact = serializers.CharField(source="name", required=False, allow_blank=True, allow_null=True)
    region = serializers.CharField(source="address", required=False, allow_blank=True, allow_null=True)
    dealerType = serializers.CharField(source="dealer_type", required=False, allow_blank=True, allow_null=True)
    totalOrders = serializers.SerializerMethodField(read_only=True)
    outstandingBalance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Dealer
        fields = [
            "id",
            "name",
            "company",
            "contact",
            "phone",
            "email",
            "address",
            "region",
            "dealerType",
            "totalOrders",
            "outstandingBalance",
            "status",
            "created_at",
            "updated_at",
        ]

    def get_totalOrders(self, _obj):
        return 0

    def get_outstandingBalance(self, _obj):
        return 0
