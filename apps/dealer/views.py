from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Dealer
from .serializers import DealerSerializer


class DealerViewSet(viewsets.ModelViewSet):
    queryset = Dealer.objects.filter(status="active")
    serializer_class = DealerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Dealer.objects.filter(status="active").order_by("-created_at")
