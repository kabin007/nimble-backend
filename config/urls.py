from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/auth/", include("apps.auth_app.urls")),
    path("api/employees/", include("apps.employee.urls")),
    path("api/bills/", include("apps.bill.urls")),
    path("api/orders/", include("apps.order.urls")),
    path("api/dealers/", include("apps.dealer.urls")),
    path("api/transactions/", include("apps.transaction.urls")),
    path("api/inventory/", include("apps.inventory.urls")),
    path("api/attendance/", include("apps.attendance.urls")),
]
