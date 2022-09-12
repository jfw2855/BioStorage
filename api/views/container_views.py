from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.container import Container
from ..serializers import ContainerSerializer, ReadContainerSerializer

"""Containers Class: CREATE container and INDEX all containers"""
class Containers(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ContainerSerializer
    def get(self, request):
        """Index request: gets all containers from db"""
        containers = Container.objects
        # Run the data through the serializer
        data = ReadContainerSerializer(containers, many=True).data
        return Response({ 'containers': data })

    def post(self, request):
        """Create request: creates a container and saves to db then returns 201"""
        container = ContainerSerializer(data=request.data['container'])
        if container.is_valid():
            container.save()
            return Response({ 'container': container.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(container.errors, status=status.HTTP_400_BAD_REQUEST)
