from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.storage import Storage
from ..serializers import StorageSerializer, ReadStorageSerializer

"""Storages Class: CREATE storages and INDEX all storages"""
class Storages(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = StorageSerializer
    def get(self, request):
        """Index request: indexes all storages from db"""
        storages = Storage.objects
        # Run the data through the serializer
        data = ReadStorageSerializer(storages, many=True).data
        return Response({ 'storages': data })

    def post(self, request):
        """Create request: creates a new storage and saves to db"""
        # Serialize/create mango
        storage = StorageSerializer(data=request.data['storage'])
        # If the mango data is valid according to our serializer...
        if storage.is_valid():
            # Save the created mango & send a response
            storage.save()
            return Response({ 'storage': storage.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(storage.errors, status=status.HTTP_400_BAD_REQUEST)

"""Storage Details Class: GET, DELETE, UPDATE specific storages (by PK)"""
class StorageDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request: Gets specific storage from db and returns serialized data"""
        storage = get_object_or_404(Storage, pk=pk)
        data = ReadStorageSerializer(storage).data
        return Response({ 'storage': data })
    
    def delete(self,request,pk):
        """Delete request: deletes storage from db then returns 204"""
        storage = get_object_or_404(Storage,pk=pk)
        storage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request: updates storage in db then returns 204"""
        storage = get_object_or_404(Storage,pk=pk)

        # Validate updates with serializer
        data = StorageSerializer(storage, data=request.data['storage'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
