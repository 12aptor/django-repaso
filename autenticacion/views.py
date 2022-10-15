from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import LoginSerializer, RegistroSerializer
from django.contrib.auth.models import User

# Create your views here.

class LoginView(TokenObtainPairView):
  permission_classes = (AllowAny,)
  serializer_class = LoginSerializer

class RegistroView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegistroSerializer
  permission_classes = (AllowAny, )