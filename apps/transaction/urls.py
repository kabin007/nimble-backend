from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TransactionViewSet,
    TransactionTypeViewSet,
    IncomeCategoryViewSet,
    ExpenseCategoryViewSet,
)


router = DefaultRouter()
router.register(r"", TransactionViewSet, basename="transaction")
router.register(r"types", TransactionTypeViewSet, basename="transaction-type")
router.register(r"categories/income", IncomeCategoryViewSet, basename="income-category")
router.register(r"categories/expense", ExpenseCategoryViewSet, basename="expense-category")

urlpatterns = [
    path("", include(router.urls)),
]
