import random
from django.conf import settings
from django.db import models
from django.db.models import Q
# Create your models here.

User = settings.AUTH_USER_MODEL # auth.User


tags_model_values = ['electronics', 'cars','boats','movies','cameras']


class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)


    def search(self,query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)


    def search(self, query, user=None):
        return self.get_queryset().search(query, user=user)

class products(models.Model):
    # pk -> integer
    # owner = models.ForeignKey(User)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)   # type: ignore
    public = models.BooleanField(default=True)

    # if just wanna print saled_price without using serializers !!
    objects= ProductManager()

    @property
    def body(self):
        return self.content
    def saled_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "123"

    def is_public(self) -> bool: 
        return self.public # True or False

    def get_tags_list(self):
        return [random.choice(tags_model_values)]

    @property
    def path(self):
        return f"/products/{self.pk}/"

    def get_absolute_url(self):
        return f"api/products/{self.pk}/"

    @property
    def endpoint(self):
        return self.get_absolute_url()
