# employee/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, EmployeeAdvanceViewSet

employee_router = DefaultRouter()
employee_router.register(r"", EmployeeViewSet, basename="employee")

advance_router = DefaultRouter()
advance_router.register(r"", EmployeeAdvanceViewSet, basename="advance")

attendance_router = DefaultRouter()
attendance_router.register(r"", AttendanceViewSet, basename="attendance")

urlpatterns = [
    path("advances/", include(advance_router.urls)),    # ← must come FIRST
    path("attendance/", include(attendance_router.urls)), # ← must come FIRST
    path("", include(employee_router.urls)),             # ← catch-all last
]