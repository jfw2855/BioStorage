from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.experiment import Experiment
from ..serializers import ExperimentSerializer

class Experiments(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ExperimentSerializer
    def get(self, request):
        """Index request"""
        exps = Experiment.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ExperimentSerializer(exps, many=True).data
        return Response({ 'experiments': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['experiment']['owner'] = request.user.id
        # Serialize/create mango
        experiment = ExperimentSerializer(data=request.data['experiment'])
        # If the mango data is valid according to our serializer...
        if experiment.is_valid():
            # Save the created mango & send a response
            experiment.save()
            return Response({ 'experiment': experiment.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(experiment.errors, status=status.HTTP_400_BAD_REQUEST)


