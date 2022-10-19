from rest_framework import generics
from .models import products
from .serializers import productSerializer


# class productsList(generics.ListCreateAPIView):
#     """
#     All products - > wount be used
#     """
#     queryset = products.objects.all()
#     serializer_class = productSerializer
#     # lookup_field = 'pk'
#     # product.objects.get(pk=1)
#     # product.objects.get(pk="abc") - > invalid lookup


class productDetailsAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    All product details .. 
    """
    queryset = products.objects.all()
    serializer_class = productSerializer


class productCreateListAPIView(generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = productSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title

        serializer.save(content=content)
