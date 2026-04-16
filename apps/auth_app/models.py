from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """User profile with role"""
    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("manager", "Manager"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="manager")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
