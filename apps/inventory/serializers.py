from rest_framework import serializers
from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    # Map frontend field names to backend
    name = serializers.CharField(source="item_name", required=True)
    unitPrice = serializers.DecimalField(source="unit_price", max_digits=10, decimal_places=2, required=True)
    reorderLevel = serializers.IntegerField(source="min_stock", required=True)
    lastUpdated = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Inventory
        fields = [
            "id",
            "name",
            "sku",
            "quantity",
            "reorderLevel",
            "unit",
            "unitPrice",
            "location",
            "description",
            "category",
            "supplier",
            "status",
            "lastUpdated",
        ]
        read_only_fields = ["id", "lastUpdated", "status"]
        extra_kwargs = {
            "location": {"required": False, "allow_blank": True},
            "description": {"required": False, "allow_blank": True},
            "supplier": {"required": False, "allow_blank": True},
            "unit": {"required": False, "allow_blank": True},
            "category": {"required": False},
        }

    def get_lastUpdated(self, obj):
        return obj.updated_at.isoformat() if obj.updated_at else obj.created_at.isoformat()

    def create(self, validated_data):
        # validated_data will have 'item_name', 'unit_price', 'min_stock' keys
        # Status defaults to 'active' in the model
        if not validated_data.get("sku"):
            import uuid
            validated_data["sku"] = str(uuid.uuid4())[:12]
        return Inventory.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

