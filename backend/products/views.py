from rest_framework import generics, mixins
from .models import products
from .serializers import productSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from api.mixins import (StaffEditorPermissionMixin,
                        UserQuerySetMixin)


class productCreateListAPIView(StaffEditorPermissionMixin,
                               UserQuerySetMixin,
                               generics.ListCreateAPIView):
    queryset = products.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title
        # very similar to form.save(), model.save()
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return products.objects.none()
    #     return qs.filter(user=request.user)


# instance for shortcuting : urls
product_list_create_view = productCreateListAPIView.as_view()


class productDetailsAPIView(UserQuerySetMixin,
                            StaffEditorPermissionMixin,
                            generics.RetrieveAPIView):
    """
    All product Detials ..
    """
    queryset = products.objects.all()
    serializer_class = productSerializer
    # lookup_field = 'pk' ??

# instance for shortcuting : urls
product_detail_view = productDetailsAPIView.as_view()


class productUpdateAPIView(UserQuerySetMixin,
                           StaffEditorPermissionMixin,
                           generics.UpdateAPIView):
    """
    Update Product 
    """
    queryset = products.objects.all()
    serializer_class = productSerializer

    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()

        # contect = title if not content
        if not instance.content:
            instance.content = instance.title


# instance for shortcuting : urls
product_update_view = productUpdateAPIView.as_view()


class productDeleteAPIView(UserQuerySetMixin,
                           StaffEditorPermissionMixin,
                           generics.DestroyAPIView):
    """
    Delete Product 
    """
    queryset = products.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'
    def perform_delete(self, instance):
        super().perform_destroy(instance)


# instance for shortcuting : urls
product_delete_view = productDeleteAPIView.as_view()


class productMixinView(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    queryset = products.objects.all()
    serializer_class = productSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):  # HTTP -> get
        # print(args, kwargs) # checking args and kwargs of retreived instance
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,  *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "product initial content"
        serializer.save(content=content)


# instance for shortcut
product_mixin_view = productMixinView.as_view()


"""The biggest difference bitween CBV and FBV is that we don't write conditions for the methods,
    we actually write function for the request methods"""


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
            title = serializer.validated_data.get('title')  # type: ignore
            content = serializer.validated_data.get(        # type: ignore
                'content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
