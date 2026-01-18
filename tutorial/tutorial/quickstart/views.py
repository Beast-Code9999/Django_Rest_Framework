from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

# import serializers
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # query set: What data am I working with
    queryset = User.objects.all().order_by("-date_joined")
    # Serializer_class: How do I format this data
    serializer_class = UserSerializer
    # Permission classes: Whos allowed to acces this
    permission_classes = [permissions.IsAuthenticated]
    
    
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]