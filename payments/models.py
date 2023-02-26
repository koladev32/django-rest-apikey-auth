from django.db import models


class Payment(models.Model):
    amount = models.FloatField()
    organization = models.ForeignKey("organization.Organization", on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)