from rest_framework import viewsets, mixins
from .models import products
from .serializers import productSerializer


class ProductViewSet(viewsets.ModelViewSet):

    """
    get -> list -> QuerySet
    get -> retrieve -> product instance detail view
    post -> create -> new instance
    put -> update
    path -> partial update
    delete -> destory

    """
    queryset = products.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'  # default


class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):

    """
    get -> list -> QuerySet
    get -> retrieve -> product instance detail view

    """
    queryset = products.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'  # default
