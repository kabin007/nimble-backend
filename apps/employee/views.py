from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee, Attendance, EmployeeAdvance
from .serializers import EmployeeSerializer, AttendanceSerializer, EmployeeAdvanceSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.exclude(status="deleted")
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Employee.objects.exclude(status="deleted").order_by("-created_at")

    @action(detail=False, methods=["get"])
    def low_staff(self, request):
        employees = self.get_queryset()
        serializer = self.get_serializer(employees, many=True)
        return Response(serializer.data)


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.request.query_params.get("employee_id")
        if employee_id:
            return Attendance.objects.filter(employee_id=employee_id).order_by("-date")
        return Attendance.objects.all().order_by("-date")


class EmployeeAdvanceViewSet(viewsets.ModelViewSet):
    queryset = EmployeeAdvance.objects.all()
    serializer_class = EmployeeAdvanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.request.query_params.get("employee_id")
        if employee_id:
            return EmployeeAdvance.objects.filter(employee_id=employee_id).order_by("-created_at")
        return EmployeeAdvance.objects.all().order_by("-created_at")
