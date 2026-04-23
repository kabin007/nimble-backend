from rest_framework import serializers
from .models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    dealerType = serializers.CharField(source="dealer_type", required=False, allow_blank=True, allow_null=True)
    totalOrders = serializers.SerializerMethodField(read_only=True)
    outstandingBalance = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Dealer
        fields = [
            "id",
            "name",
            "phone",
            "email",
            "address",
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
