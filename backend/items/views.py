from django.shortcuts import render
from .serializers import itemsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import items
from rest_framework import serializers
from rest_framework import status
from django.shortcuts import get_object_or_404

"""Full CRUD With FBV"""


# OverView
@api_view(['GET'])
def apiOverView(request):
    """
    Shopping Items
    """
    api_urls = {
        # pk -> primary key which unique identifying item you search for
        'All-Items': 'all/',
        'Search by Category': '/?category=category_name/',
        'Search by SubCategory': '/?category=category_name/',
        'Add': '/create/',
        'Update': '/update/pk/',
        'Delete': '/item/pk/delete/',

    }
    return Response(api_urls)


# Create View
@api_view(['GET', 'POST'])
def add_items(request):
    item = itemsSerializers(data=request.data)

    # validate if item exists
    if items.objects.filter(**request.data).exists():
        raise serializers.ValidationError(
            "This Item Already Exists!")  # type: ignore

    if item.is_valid():
        item.save()
        return Response(item.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_items(request):
    """
    Search by Category ->>  /?category=category_name/
    Search by SubCategory ->> /?category=category_name/
    """

    # checking for the parameters from the URL
    # if request.query_params:
    #     allItems = items.objects.filter(**request.query_param.dict())
    # else:
    allItems = items.objects.all()
    serializer = itemsSerializers(allItems, many=True)

    # if there is something in items else raise error
    if allItems:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#Update View
@api_view(['GET', 'PUT'])
def update_items(request, pk):
    wantedItem = items.objects.get(pk=pk)
    data = itemsSerializers(instance=wantedItem, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Delete View
@api_view(['GET', 'DELETE'])
def delete_items(request, pk):
    wantedItem = get_object_or_404(items, pk=pk)
    wantedItem.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
