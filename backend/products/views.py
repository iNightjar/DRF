from rest_framework import generics
from .models import products
from .serializers import productSerializer


class productDetailAPIView(generics.RetrieveAPIView):
    """
    All product details .. 
    """
    queryset = products.objects.all()
    serializer_class = productSerializer
    # lookup_field = 'pk'
    # product.objects.get(pk=1)
    # product.objects.get(pk="abc") - > invalid lookup
