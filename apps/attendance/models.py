from django.db import models
from apps.core.models import BaseModel
from apps.employee.models import Attendance as EmployeeAttendance


# Attendance is handled in employee app, this is just a placeholder
class AttendanceProxy(EmployeeAttendance):
    class Meta:
        proxy = True
        db_table = "attendance"
