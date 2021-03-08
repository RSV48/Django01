from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='наиментование категории', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание категории', blank=True)
    create_dt = models.DateTimeField(verbose_name='дата создания категории', auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='наименование продука', max_length=128)
    image = models.ImageField(upload_to='product_images', blank=True)
    short_desc = models.CharField(verbose_name='кратокое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
