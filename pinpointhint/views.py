from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets, generics
from .serializers import UserSerializer, GroupSerializer


from .serializers import *



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

    def get_queryset(self):
        queryset = Pins.objects.all()
        return queryset
