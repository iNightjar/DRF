from django.db import models

# Create your models here.


class products(models.Model):
    # pk -> integer
    # owner = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)  # type: ignore

    # if just wanna print saled_price without using serializers !!

    @property
    def saled_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "123"
