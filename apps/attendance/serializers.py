from rest_framework import serializers
from apps.employee.models import Attendance, Employee


class AttendanceSerializer(serializers.ModelSerializer):
    employeeId = serializers.PrimaryKeyRelatedField(source="employee", queryset=Employee.objects.all())

    class Meta:
        model = Attendance
        fields = ["id", "employeeId", "date", "status", "notes", "created_at", "updated_at"]
