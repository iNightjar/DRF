from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import products

# def validate_title(value):
#     queryset = products.objects.filter(title__iexact=value)
#     if queryset.exists():
#         raise serializers.ValidationError(f"{value} is already a product name.")
#     return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError(f"Hello is not allowed")
    return value


unique_product_title = UniqueValidator(queryset=products.objects.all())
