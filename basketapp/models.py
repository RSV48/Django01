from django.conf import settings
from django.db import models

from mainapp.models import Product


class BasketQuerySet(models.QuerySet):

    def delete(self, *args, **kwargs):
        for item in self:
            item.product.quantity += item.quantity
            item.product.save()
        super().delete()


class Basket(models.Model):
    objects = BasketQuerySet.as_manager()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(auto_now_add=True, verbose_name='время')


    @property
    def product_cost(self):
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        _item = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _item)))
        return _total_quantity

    @property
    def total_cost(self):
        _item = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _item)))
        return _total_cost

    def save(self, *args, **kwargs):
        if self.pk:
            self.product.quantity -= self.quantity - self.__class__.get_item(self.pk).quantity
        else:
            self.product.quantity -= self.quantity
        self.product.save()
        super(self.__class__, self).save(*args, **kwargs)
