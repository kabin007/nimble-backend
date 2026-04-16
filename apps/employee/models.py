from django.db import models
from apps.core.models import BaseModel


class Employee(BaseModel):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    join_date = models.CharField(max_length=50, blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[("active", "Active"), ("inactive", "Inactive"), ("deleted", "Deleted")],
        default="active",
    )

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name


class Attendance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendance")
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("present", "Present"), ("absent", "Absent"), ("leave", "Leave")],
        default="absent",
    )
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "attendance"
        unique_together = ("employee", "date")

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"


class EmployeeAdvance(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="advances")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[("pending", "Pending"), ("approved", "Approved"), ("rejected", "Rejected")],
        default="pending",
    )
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "employee_advance"

    def __str__(self):
        return f"{self.employee.name} - {self.amount} - {self.status}"
