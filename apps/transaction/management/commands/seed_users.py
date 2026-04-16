from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.auth_app.models import UserProfile


class Command(BaseCommand):
    help = "Seed test users"

    def handle(self, *args, **options):
        # Create owner user
        owner, created = User.objects.get_or_create(
            username="owner",
            defaults={"email": "owner@nimblegarment.com", "is_staff": False},
        )
        if created:
            owner.set_password("owner123")
            owner.save()
            UserProfile.objects.create(user=owner, role="owner")
            self.stdout.write(f"Created owner user: owner / owner123")
        else:
            self.stdout.write("Owner user already exists")

        # Create manager user
        manager, created = User.objects.get_or_create(
            username="manager",
            defaults={"email": "manager@nimblegarment.com", "is_staff": False},
        )
        if created:
            manager.set_password("manager123")
            manager.save()
            UserProfile.objects.create(user=manager, role="manager")
            self.stdout.write(f"Created manager user: manager / manager123")
        else:
            self.stdout.write("Manager user already exists")

        user, created= User.objects.get_or_create(
            username="kushal",
            defaults={"email": "kushal@nimblegarment.com", "is_staff": False},
        )
        if created:
            user.set_password("kushal123")
            user.save()
            UserProfile.objects.create(user=user, role="user")
            self.stdout.write(f"Created user: kushal / kushal123")

        self.stdout.write(self.style.SUCCESS("Successfully seeded users"))
