import csv

from django.core.management.base import BaseCommand

from ...models import Contact, Role, Agency




class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **kwargs):
        file_name = kwargs["file_name"]
        with open(f"{file_name}", "r") as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    contact = row[0]
                    tel = row[1]
                    role = Role.objects.get(pk=int(row[2]))
                    agency = Agency.objects.get(pk=int(row[3]))
                    # print(contact)
                    Contact.objects.get_or_create(
                        contact=contact,
                        tel=tel,
                        role=role,
                        agency=agency
                    )
                    self.stdout.write(self.style.SUCCESS(f"{contact} added"))