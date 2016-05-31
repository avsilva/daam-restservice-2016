from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets, generics
from .serializers import UserSerializer, GroupSerializer
from rest_framework_gis.filters import DistanceToPointFilter


from .serializers import *
import logging
logging.basicConfig(filename='/tmp/debug.log',level=logging.INFO)



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PinsGeoJson(generics.ListCreateAPIView):

    queryset = Pins.objects.all()
    serializer_class = PinPointSerializer

    distance_filter_field = 'geom'
    filter_backends = (DistanceToPointFilter, )
    bbox_filter_include_overlapping = True # Optional
    distance_filter_convert_meters = True

    def get_queryset(self):
        queryset = Pins.objects.all()
        #radius = self.request.query_params.get('radius', None)
        #logging.info('RADIUS '+str(radius))
        return queryset

class PinsGeoJsonDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Pins.objects.all()
    serializer_class = PinPointDetailSerializer
