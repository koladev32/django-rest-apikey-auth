from django.db import models

from rest_framework_simple_api_key.models import AbstractAPIKey


class Organization(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


class OrganizationAPIKey(AbstractAPIKey):
    entity = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )
