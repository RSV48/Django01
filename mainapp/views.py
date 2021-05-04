import json
import os
import random

from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory


# def get_basket(user):
#     if user.is_authenticated:
#         return Basket.objects.filter(user=user)
#     return []


def get_hot_product():
    products = Product.objects.all().select_related()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]


def main(request):
    # basket = get_basket(request.user)
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:4]
    contante = {
        'title': 'Главная',
        'products': products,
    }
    return render(request, 'mainapp/index.html', contante)


def products(request, pk=None, page=1):
    links_menu = ProductCategory.objects.all()
    title = 'продукты'
    # basket = get_basket(request.user)
    hot_product = get_hot_product()

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.filter(is_active=True, category__is_active=True).order_by('price').\
                select_related('Category')
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category=category_item, is_active=True, category__is_active=True).\
                select_related()
        paginator = Paginator(product_list,2)
        try:
            product_paginator = paginator.page(page)
        except PageNotAnInteger:
            product_paginator = paginator.page(1)
        except EmptyPage:
            product_paginator = paginator.page(paginator.num_pages)
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category_item,
            'products': product_paginator,

        }
        return render(request, 'mainapp/products_list.html', content)
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': get_same_products(hot_product),
    }
    return render(request, 'mainapp/products.html', content)


def product(request, pk):

    product = get_object_or_404(Product, pk=pk)
    title = product.name
    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': product,
        'same_products': get_same_products(product),
    }
    return render(request, 'mainapp/product.html', content)


def contact(request):
    location = []
    # basket = get_basket(request.user)
    with open(os.path.join(settings.BASE_DIR, 'mainapp/templates/mainapp/contacts.json')) as read_file:
        location = json.load(read_file)
    contante = {
        'title': 'Контакты',
        'location_contacts': location,
    }
    return render(request, 'mainapp/contact.html', contante)

# Create your views here.
