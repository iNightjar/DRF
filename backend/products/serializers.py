from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import products
from . import validators
from api.serializers import UserPublicSerializer


class productSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user',  read_only=True)

    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail',
                                               lookup_field='pk'
                                               )
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
                                              validators.unique_product_title])

    class Meta:
        model = products
        fields = [
            'owner',  # user_id
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',

        ]
    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }
    
    def get_edit_url(self, obj):
        # return f"/api/v2/products/{obj.pk}/"
        request = self.context.get('request')  # serlf.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
