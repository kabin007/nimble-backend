from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, EmployeeAdvanceViewSet

router = DefaultRouter()
router.register(r"", EmployeeViewSet, basename="employee")
router.register(r"attendance", AttendanceViewSet, basename="attendance")
router.register(r"advances", EmployeeAdvanceViewSet, basename="advance")

urlpatterns = [
    path("", include(router.urls)),
]
