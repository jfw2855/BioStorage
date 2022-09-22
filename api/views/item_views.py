from urllib import response
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.item import Item
from ..serializers import ItemSerializer, ReadItemSerializer

"""Item Class: CREATE items and INDEX all items"""
class Items(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ItemSerializer
    
    def get(self, request):
        """Index request: indexes all items"""
        items = Item.objects
        data = ReadItemSerializer(items, many=True).data
        return Response({ 'items': data })

    def post(self, request):
        """Create request: creates a new item then saves to db"""
        item = ItemSerializer(data=request.data['item'])
        if item.is_valid():
            item.save()
            return Response({ 'item': item.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)

"""Storage Item Class: INDEX all storage items"""
class StorageItemsDetails(generics.ListAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ItemSerializer

    def get(self, request, pk):
        """ Index request: indexes all items within a storage"""
        items = Item.objects.filter(storage_id=pk)
        data = ReadItemSerializer(items, many=True).data
        return Response({'storage_items': data})

"""Container Item Class: INDEX all container items"""
class ContainerItemsDetails(generics.ListAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ItemSerializer

    def get(self, request, pk):
        """ Index request: indexes all items within a container"""
        items = Item.objects.filter(container_id=pk)
        data = ReadItemSerializer(items, many=True).data
        return Response({'container_items': data})

"""User Items Class: INDEX all user items"""
class UserItemsDetails(generics.ListAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ItemSerializer

    def get(self, request):
        """ Index request: indexes all user items"""
        items = Item.objects.filter(owner=request.user.id)
        print(request.user.id)
        data = ReadItemSerializer(items, many=True).data
        return Response({'user_items': data})

"""Item Details Class: GET, DELETE, UPDATE specific items (by PK)"""
class ItemDetails (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, pk):
        """Show request: get data then return serialized data"""
        item = get_object_or_404(Item, pk=pk)
        data = ReadItemSerializer(item).data
        return Response({'item':data})
    
    def delete(self,request, pk):
        """Delete Request: deletes requester's item data from db then return 204"""
        item = get_object_or_404(Item, pk=pk)
        #checks if requester is owner (if owner exists) of item before deleting
        if item.owner and request.user != item.owner:
            raise PermissionDenied("Unauthorized, you do not own this item") 
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request: updates the item then returns 204"""
        item = get_object_or_404(Item, pk=pk)
        # Checks if user is item owner (if owner exists)
        if item.owner and request.user != item.owner:
            raise PermissionDenied('Unauthorized, you do not own this item')
        # Validate updates with serializer
        data = ItemSerializer(item, data=request.data['item'], partial=True)
        if data.is_valid():
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)