from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Transaction, TransactionType, IncomeCategory, ExpenseCategory
from .serializers import (
    TransactionSerializer,
    TransactionTypeSerializer,
    IncomeCategorySerializer,
    ExpenseCategorySerializer,
)


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.filter(status="active")
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(status="active").order_by("-date")

    def perform_destroy(self, instance):
        """Soft delete by marking transaction as deleted"""
        instance.status = "deleted"
        instance.save()

    @action(detail=False, methods=["get"])
    def by_type(self, request):
        type_name = request.query_params.get("type")
        if not type_name:
            return Response({"error": "type is required"}, status=status.HTTP_400_BAD_REQUEST)

        transactions = Transaction.objects.filter(type=type_name, status="active").order_by("-date")
        serializer = self.get_serializer(transactions, many=True)
        return Response(serializer.data)


class TransactionTypeViewSet(viewsets.ModelViewSet):
    queryset = TransactionType.objects.all()
    serializer_class = TransactionTypeSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def with_categories(self, request):
        """Get all transaction types with their categories"""
        types = TransactionType.objects.all()
        data = []
        for t in types:
            type_data = TransactionTypeSerializer(t).data
            type_data["income_categories"] = IncomeCategorySerializer(
                t.income_categories.all(), many=True
            ).data
            type_data["expense_categories"] = ExpenseCategorySerializer(
                t.expense_categories.all(), many=True
            ).data
            data.append(type_data)
        return Response(data)

    @action(detail=False, methods=["get"], url_path="by-name/(?P<name>[^/]+)")
    def by_name(self, request, name=None):
        """Get transaction type and its categories by name"""
        try:
            trans_type = TransactionType.objects.get(name=name)
            data = TransactionTypeSerializer(trans_type).data
            data["income_categories"] = IncomeCategorySerializer(
                trans_type.income_categories.all(), many=True
            ).data
            data["expense_categories"] = ExpenseCategorySerializer(
                trans_type.expense_categories.all(), many=True
            ).data
            return Response(data)
        except TransactionType.DoesNotExist:
            return Response(
                {"error": "Transaction type not found"}, status=status.HTTP_404_NOT_FOUND
            )


class IncomeCategoryViewSet(viewsets.ModelViewSet):
    queryset = IncomeCategory.objects.all()
    serializer_class = IncomeCategorySerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def by_type(self, request):
        """Get all income categories for a transaction type"""
        type_id = request.query_params.get("type_id")
        if type_id:
            categories = IncomeCategory.objects.filter(transaction_type_id=type_id)
        else:
            categories = IncomeCategory.objects.all()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def by_type(self, request):
        """Get all expense categories for a transaction type"""
        type_id = request.query_params.get("type_id")
        if type_id:
            categories = ExpenseCategory.objects.filter(transaction_type_id=type_id)
        else:
            categories = ExpenseCategory.objects.all()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

