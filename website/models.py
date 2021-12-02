from django.db import models


class Package(models.Model):
    package = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    services = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.package


class Location(models.Model):
    branch_name = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    # Contacts
    contact_person_1 = models.CharField(max_length=100, blank=True, null=True)
    contact_number_1 = models.CharField(max_length=10, blank=True, null=True)
    contact_person_2 = models.CharField(max_length=100, blank=True, null=True)
    contact_number_2 = models.CharField(max_length=10, blank=True, null=True)
    contact_person_3 = models.CharField(max_length=100, blank=True, null=True)
    contact_number_3 = models.CharField(max_length=10, blank=True, null=True)
    contact_person_4 = models.CharField(max_length=100, blank=True, null=True)
    contact_number_4 = models.CharField(max_length=10, blank=True, null=True)
    contact_person_5 = models.CharField(max_length=100, blank=True, null=True)
    contact_number_5 = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.branch_name
