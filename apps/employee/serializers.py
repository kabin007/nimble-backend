from rest_framework import serializers
from .models import Employee, Attendance, EmployeeAdvance


class EmployeeSerializer(serializers.ModelSerializer):
    joinDate = serializers.CharField(source="join_date", required=False, allow_blank=True, allow_null=True)
    profilePicture = serializers.CharField(source="profile_picture", required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Employee
        fields = [
            "id",
            "name",
            "role",
            "department",
            "phone",
            "email",
            "salary",
            "joinDate",
            "profilePicture",
            "status",
            "created_at",
            "updated_at",
        ]


class AttendanceSerializer(serializers.ModelSerializer):
    employeeId = serializers.PrimaryKeyRelatedField(source="employee", queryset=Employee.objects.all())

    class Meta:
        model = Attendance
        fields = ["id", "employeeId", "date", "status", "notes", "created_at", "updated_at"]


class EmployeeAdvanceSerializer(serializers.ModelSerializer):
    employeeId = serializers.PrimaryKeyRelatedField(source="employee", queryset=Employee.objects.all())
    reason = serializers.CharField(source="notes", required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = EmployeeAdvance
        fields = ["id", "employeeId", "amount", "date", "status", "reason", "created_at", "updated_at"]
