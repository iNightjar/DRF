from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL # auth.User
class products(models.Model):
    # pk -> integer
    # owner = models.ForeignKey(User)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)   # type: ignore

    # if just wanna print saled_price without using serializers !!

    @property
    def saled_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "123"