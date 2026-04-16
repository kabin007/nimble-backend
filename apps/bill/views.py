from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Bill
from .serializers import BillSerializer


class BillViewSet(viewsets.ModelViewSet):
    queryset = Bill.objects.filter(record_status="active")
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bill.objects.filter(record_status="active").order_by("-created_at")
