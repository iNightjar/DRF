from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import products


class productSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',
     lookup_field='pk'
     )

    class Meta:
        model = products
        fields = [
            'url', 'edit_url', 'pk', 'title', 'content', 'price', 'my_discount'
        ]

    def get_edit_url(self, obj):
        # return f"/api/v2/products/{obj.pk}/"
        request = self.context.get('request') # serlf.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        # print(obj.id)
        """
        obj.user - > user.username
        """
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, products):
            return None

        return obj.get_discount()