from rest_framework import serializers
from .models import products


class productSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = products
        fields = [
            'title', 'content', 'price','my_discount'
        ]

    def get_my_discount(self, obj):
        # print(obj.id)
        """
        obj.user - > user.username
        """
        return obj.get_discount()
