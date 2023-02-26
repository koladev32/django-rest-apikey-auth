from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework.response import Response


class OrganizationViewSet(viewsets.ViewSet):

    http_method_names = ['post']

    @action(methods=['post'], detail=True)
    def create_api_key(self, request, *args, **kwargs):
        pass


