"""
Seializers are more like forms here
"""

from http.client import ImproperConnectionState
from django import forms
from .models import products


class productForm(forms.ModelForm):
    class Meta:
        model = products
        fields = [
            'title', 'content', 'price'
        ]
