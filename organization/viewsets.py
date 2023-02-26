from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework import status

from organization.models import OrganizationAPIKey


class OrganizationViewSet(viewsets.ViewSet):
    http_method_names = ["post"]

    @action(methods=["post"], detail=True)
    def create_api_key(self, pk, request, *args, **kwargs):
        _, key = OrganizationAPIKey.objects.create_api_key(
            name="Org Api Key", organization_id=pk
        )

        return Response({"key": key}, status=status.HTTP_201_CREATED)
