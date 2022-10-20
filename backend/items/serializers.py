from dataclasses import fields
from http.client import ImproperConnectionState
from rest_framework import serializers
from .models import items

class itemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = items
        fields = ('category', 'subcategory', 'name', 'amount')
