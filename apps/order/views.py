from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(record_status="active")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(record_status="active").order_by("-created_at")
