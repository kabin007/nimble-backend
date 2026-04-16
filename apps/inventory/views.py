from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import models
from .models import Inventory
from .serializers import InventorySerializer


class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.filter(status="active")
    serializer_class = InventorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Inventory.objects.filter(status="active").order_by("-created_at")

    @action(detail=False, methods=["get"])
    def low_stock(self, request):
        inventory = Inventory.objects.filter(
            status="active",
            quantity__lte=models.F("min_stock")
        )
        serializer = self.get_serializer(inventory, many=True)
        return Response(serializer.data)

