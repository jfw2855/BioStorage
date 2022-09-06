from urllib import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.storage_type import StorageType
from ..serializers import StorageTypeSerializer

class StorageTypes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = StorageTypeSerializer
    
    def get(self, request):
        """Index request: indexes all storage types"""
        types = StorageType.objects
        data = StorageTypeSerializer(types, many=True).data
        return Response({ 'storage_types': data })

    def post(self, request):
        """Create request: creates new storage type then saves to db"""
        type = StorageTypeSerializer(data=request.data['storage_type'])
        if type.is_valid():
            type.save()
            return Response({ 'storage_type': type.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(type.errors, status=status.HTTP_400_BAD_REQUEST)

class StorageTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request: gets storage type from db"""
        type = get_object_or_404(StorageType, pk=pk)
        data = StorageTypeSerializer(type).data
        return Response({ 'storage_type': data })

    def delete(self,request,pk):
        """Delete request: deletes storage type from db then returns 204"""
        type = get_object_or_404(StorageType,pk=pk)
        type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request: updates storage type in db then returns 204"""
        type = get_object_or_404(StorageType,pk=pk)

        # Validate updates with serializer
        data = StorageTypeSerializer(type, data=request.data['storage_type'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
