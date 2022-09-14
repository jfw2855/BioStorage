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

