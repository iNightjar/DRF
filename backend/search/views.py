from rest_framework import generics
from products.models import products
from products.serializers import productSerializer

class SearchListView(generics.ListAPIView):
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