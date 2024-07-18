from rest_framework import serializers
from django.contrib.auth.models import User
from decimal import Decimal

from .models import Category, MenuItem, Cart, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


