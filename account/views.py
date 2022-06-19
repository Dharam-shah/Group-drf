from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User,Group
from .serializers import UserSignupSerializer,GroupSerializer, UserSerializer
from account import serializers
from rest_framework.views import APIView
# Create your views here.



class UsersListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSignupViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
