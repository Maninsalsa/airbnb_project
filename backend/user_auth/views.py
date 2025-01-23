from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
