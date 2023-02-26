from rest_framework import viewsets
from rest_framework_simple_api_key.permissions import IsActiveEntity

from organization.backend import OrganizationAPIKeyAuthentication
from payments.models import Payment
from payments.serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    authentication_classes = (OrganizationAPIKeyAuthentication,)
    permission_classes = (IsActiveEntity,)
    serializer_class = PaymentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Payment.objects.all()

        return Payment.objects.filter(organization=self.request.user)
