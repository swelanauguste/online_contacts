from tabnanny import verbose

from django.db import models


class Agency(models.Model):
    agency = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "agencies"

    def __str__(self):
        return f"({self.id}) - {self.agency}"


class Role(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return f"({self.id}) - {self.role}"


class Contact(models.Model):
    contact = models.CharField(max_length=255, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True, blank=True)
    tel = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.contact} - ({self.tel})"
