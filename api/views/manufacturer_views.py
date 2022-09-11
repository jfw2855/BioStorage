from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

#imports model and serializer
from ..models.manufacturer import Manufacturer
from ..serializers import ManufacturerSerializer

"""Manufacturers Class: CREATE storages and INDEX all manufacturers"""
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

"""Manufacturer Details Class: GET, DELETE, UPDATE specific manufacturer (by PK)"""
class ManufacturerDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request: Gets specific manufacturer from db and returns serialized data"""
        mf = get_object_or_404(Manufacturer, pk=pk) #mf == manufacturer
        data = ManufacturerSerializer(mf).data
        return Response({ 'manufacturer': data })
    
    def delete(self,request,pk):
        """Delete request: deletes manufacturer from db then returns 204"""
        mf = get_object_or_404(Manufacturer,pk=pk)
        mf.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request: updates manufacturer in db then returns 204"""
        mf = get_object_or_404(Manufacturer,pk=pk)

        # Validate updates with serializer
        data = ManufacturerSerializer(mf, data=request.data['manufacturer'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
