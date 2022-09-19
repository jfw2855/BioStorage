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


