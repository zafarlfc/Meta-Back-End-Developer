from django.shortcuts import render
from rest_framework import generics

from .models import MenuItems
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemSerializer