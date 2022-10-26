from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import products
from . import validators


class productSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',
     lookup_field='pk'
     )
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
                                              validators.unique_product_title])
    name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model = products
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'name',
            'content',
            'price',
            'my_discount'
        ]

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = products.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(
    #             f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     # return products.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     # return super().update(instance, validated_data)
    #     # instance.title = validated_data.get('title')
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

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

