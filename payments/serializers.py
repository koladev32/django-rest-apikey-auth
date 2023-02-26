from rest_framework import serializers

from organization.models import Organization


class PaymentSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all()
    )

    class Meta:
        model = Organization
        fields = "__all__"
