from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from diplomas.models import Diploma
from django.utils import timezone


class Command(BaseCommand):
    help = "Create sample diplomas"

    def handle(self, *args, **options):
        User = get_user_model()
        user, _ = User.objects.get_or_create(username="demo", defaults={"password": "demo"})
        for i in range(1, 6):
            Diploma.objects.get_or_create(
                diploma_number=f"D{i:03}",
                defaults={
                    "full_name": f"User {i}",
                    "issue_date": timezone.now().date(),
                    "diploma_file": "diplomas/sample.pdf",
                    "created_by": user,
                },
            )
        self.stdout.write(self.style.SUCCESS("Test data created"))
