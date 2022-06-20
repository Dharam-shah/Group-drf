from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .serializers import UserSignupSerializer, GroupSerializer, UserSerializer
from rest_framework.views import APIView

# Create your views here.
class UsersListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def get_queryset(self):
        # users = Group.objects.filter(id=self.kwargs.get('id'))
        #results = User.objects.filter(groups__name='group1')
        users = User.objects.filter(groups__name='group1')
        #import ipdb; ipdb.set_trace()
        return users

class UserSignupViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer


