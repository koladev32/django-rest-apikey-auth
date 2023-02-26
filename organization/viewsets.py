from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework import status

from organization.models import OrganizationAPIKey, Organization


class OrganizationViewSet(viewsets.ModelViewSet):
    http_method_names = ["post"]
    queryset = Organization.objects.all()

    @action(methods=["post"], detail=True)
    def create_api_key(self, request, *args, **kwargs):
        organization = self.get_object()
        _, key = OrganizationAPIKey.objects.create_api_key(
            name="Org Api Key", organization=organization
        )

        return Response({"key": key}, status=status.HTTP_201_CREATED)
