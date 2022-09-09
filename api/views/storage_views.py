from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.storage import Storage
from ..serializers import StorageSerializer

"""Storages Class: CREATE storages and INDEX all storages"""
class Storages(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = StorageSerializer
    def get(self, request):
        """Index request"""
        storages = Storage.objects
        # Run the data through the serializer
        data = StorageSerializer(storages, many=True).data
        return Response({ 'storages': data })

    def post(self, request):
        """Create request"""
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
        data = StorageSerializer(storage).data
        return Response({ 'storage': data })
