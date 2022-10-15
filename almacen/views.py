from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductosSerializer, CategoriasSerializer
from .models import Productos, Categorias

# Create your views here.

class ProductosView(generics.ListCreateAPIView):
  queryset = Productos.objects.all()
  serializer_class = ProductosSerializer

class CategoriasView(generics.ListCreateAPIView):
  queryset = Categorias.objects.all()
  serializer_class = CategoriasSerializer