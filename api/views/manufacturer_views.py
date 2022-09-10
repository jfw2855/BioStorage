from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

#imports model and serializer
from ..models.manufacturer import Manufacturer
from ..serializers import ManufacturerSerializer

"""Storages Class: CREATE storages and INDEX all manufacturers"""
class Manufacturers(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ManufacturerSerializer
    def get(self, request):
        """Index request: returns an index of all manufactuerers in db"""
        mfs = Manufacturer.objects  #mfs == Manufacturers
        # Run the data through the serializer
        data = ManufacturerSerializer(mfs, many=True).data
        return Response({ 'manufacturers': data })

    def post(self, request):
        """Create request: creates new manufactuerer in db then returns 201"""
        mf = ManufacturerSerializer(data=request.data['manufacturer']) #mf == manufactuerer
        if mf.is_valid():
            mf.save()
            return Response({ 'manufactuerer': mf.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(mf.errors, status=status.HTTP_400_BAD_REQUEST)