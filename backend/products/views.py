from rest_framework import generics
from .models import products
from .serializers import productSerializer
from rest_framework.decorators import api_view
# from django.http import Http404
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import serializers

class productDetailsAPIView(generics.RetrieveAPIView):
    """
    All product Detials .. You can Modify Or Delete 
    """
    queryset = products.objects.all()
    serializer_class = productSerializer

# instance for shortcuting : urls
product_detail_view = productDetailsAPIView.as_view()


class productUpdateAPIView(generics.UpdateAPIView):
    """
    Update Product 
    """
    queryset = products.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance= serializer.save()
        
        # contect = title if not content
        if not instance.content:
            instance.content = instance.title

# instance for shortcuting : urls
product_update_view = productUpdateAPIView.as_view()


class productDeleteAPIView(generics.DestroyAPIView):
    """
    Delete Product 
    """
    queryset = products.objects.all()
    serializer_class = productSerializer

    def perform_delete(self, instance):
        super().perform_destroy(instance)
        

# instance for shortcuting : urls
product_delete_view = productDeleteAPIView.as_view()

class productCreateListAPIView(generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = productSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title

        serializer.save(content=content)
product_list_create_view = productCreateListAPIView.as_view()




# first creating FBV for create and list
# all crud in FBV
@api_view(['POST', 'GET', 'PUT', 'DELETE'])
def create_list_FBV(request, pk=None, *args, **kwargs):
    """
    Using Function Based Views for Listing and Creating
    """

    # checking the request itself
    method = request.method  # type: ignore
    # if wanna to view all or specific products
    if method == "GET":
        # url_args??
        # get request -> detail view
        # list view
        if pk is not None:
            qs = get_object_or_404(products, pk=pk)
            dataRetrieved = productSerializer(qs).data
            return Response(dataRetrieved)
        # list all
        qs = products.objects.all()
        dataRetrieved = productSerializer(qs, many=True).data
        return Response(dataRetrieved)

    # if wanna to create or insert
    if method == "POST":
        serializer = productSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
