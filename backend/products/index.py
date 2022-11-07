from algoliasearch_django import AlgoliaIndex
from .models import products
from algoliasearch_django.decorators import register


@register(products)
class ProductIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public',

    ]

    tags = 'get_tags_list'

#admin.site.register(product, ProductModelAdmin)
 