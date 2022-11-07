from rest_framework import generics
from products.models import products
from products.serializers import productSerializer
from rest_framework.response import Response
from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=400)
        results = client.perfom_search(query, tags=tag)
        return Response(results)


class SearchListOldView(generics.ListAPIView):
    queryset = products.objects.all()
    serializer_class = productSerializer
    
    def get_queryset(self,*args, **kwargs):
        qs= super().get_queryset(*args, **kwargs)
        q = self.request.GET.get('q')
        results = products.objects.none()
        if q is not None:
            user = None
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(q, user=user)
        return results