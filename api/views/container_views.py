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


"""Container Details Class: GET, DELETE, UPDATE specific containers (by PK)"""
class ContainerDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request: Gets specific container from db and returns serialized data"""
        container = get_object_or_404(Container, pk=pk)
        data = ReadContainerSerializer(container).data
        return Response({ 'container': data })
    
    def delete(self,request,pk):
        """Delete request: deletes container from db then returns 204"""
        container = get_object_or_404(Container,pk=pk)
        container.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request: updates container in db then returns 204"""
        container = get_object_or_404(Container,pk=pk)

        # Validate updates with serializer
        data = ContainerSerializer(container, data=request.data['container'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
