from rest_framework import serializers

from .models import MenuItems

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = "__all__"
