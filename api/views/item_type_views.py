from urllib import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.item_type import ItemType
from ..serializers import ItemTypeSerializer

"""Item Types Class: CREATE item types and INDEX all item types"""
class ItemTypes(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ItemTypeSerializer
    
    def get(self, request):
        """Index request: indexes all item types"""
        types = ItemType.objects
        data = ItemTypeSerializer(types, many=True).data
        return Response({ 'item_types': data })

    def post(self, request):
        """Create request: creates new item type then saves to db"""
        type = ItemTypeSerializer(data=request.data['item_type'])
        if type.is_valid():
            type.save()
            return Response({ 'item_type': type.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(type.errors, status=status.HTTP_400_BAD_REQUEST)

"""Item Type Details Class: GET, DELETE, UPDATE specific item types (by PK)"""
class ItemTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request: Gets specific item type from db and returns serialized data"""
        type = get_object_or_404(ItemType, pk=pk)
        data = ItemTypeSerializer(type).data
        return Response({ 'item_type': data })
    
    def delete(self,request,pk):
        """Delete request: deletes item type from db then returns 204"""
        type = get_object_or_404(ItemType,pk=pk)
        type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request: updates item type in db then returns 204"""
        type = get_object_or_404(ItemType,pk=pk)

        # Validate updates with serializer
        data = ItemTypeSerializer(type, data=request.data['item_type'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
