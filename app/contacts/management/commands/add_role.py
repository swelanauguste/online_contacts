from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from ...models import Role


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}") as file:
            for row in file:
                role = row.lower().replace("\n", "")
                self.stdout.write(self.style.SUCCESS(f"{role} added"))
                Role.objects.get_or_create(role=role)
        self.stdout.write(self.style.SUCCESS("list of objects added"))