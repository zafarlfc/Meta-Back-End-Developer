from rest_framework import serializers
from django.contrib.auth.models import User
from decimal import Decimal

from .models import Category, MenuItem, Cart, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):
    query_set = Category.objects.all()
    category = serializers.PrimaryKeyRelatedField(queryset=query_set)

    # category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = "__all__"


class UserSerilializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
