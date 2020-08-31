from django.shortcuts import render 
from MyApp.models import ProductInfo
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import generics
from .serializers import ProductInfoSerializer

class ProductInfoViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

class ProductInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer
    # permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

