from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

#imports model and serializer
from ..models.category import Category
from ..serializers import CategorySerializer

"""Categories Class: CREATE categories and INDEX all categories"""
class Categories(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CategorySerializer
    def get(self, request):
        """Index request: returns an index of all categories in db"""
        cats = Category.objects  #cats == categories
        # Run the data through the serializer
        data = CategorySerializer(cats, many=True).data
        return Response({ 'categories': data })

    def post(self, request):
        """Create request: creates new category in db then returns 201"""
        cat = CategorySerializer(data=request.data['category']) #cat == category
        if cat.is_valid():
            cat.save()
            return Response({ 'category': cat.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(cat.errors, status=status.HTTP_400_BAD_REQUEST)