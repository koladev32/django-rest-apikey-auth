from rest_framework import viewsets
from rest_framework_simple_api_key.backends import APIKeyAuthentication
from rest_framework_simple_api_key.permissions import IsActiveEntity

from payments.models import Payment


class PaymentViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post"]
    queryset = Payment.objects.all()
    authentication_classes = (APIKeyAuthentication,)
    permission_classes = (IsActiveEntity,)
