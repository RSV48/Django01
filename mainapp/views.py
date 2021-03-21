import json
import os

from django.conf import settings
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory



def main(request):
    products = Product.objects.all()[:4]
    contante = {
        'title': 'Главная',
        'products':products
    }
    return render(request, 'mainapp/index.html', contante)


def products(request, pk=None):

    basket_quantity = 0
    basket_cost = 0
    if request.user.is_authenticated:
        basket_quantity = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat=True)))
        basket_cost = sum(list(Basket.objects.filter(user=request.user).values_list('cost', flat=True)))
    links_menu = ProductCategory.objects.all()
    title = 'продукты'

    if pk is not None:
        if pk == 0:
            product_list = Product.objects.all().order_by('price')
            category_item ={'name':'все', 'pk': 0}
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            product_list = Product.objects.filter(category=category_item)
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category_item,
            'products': product_list,
            'basket_quantity': basket_quantity,
            'basket_cost': basket_cost

        }
        print(content)
        return render(request,'mainapp/products_list.html', content)

    same_products = Product.objects.all()[:3]
    content = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'same_products':same_products,
        'basket_quantity': basket_quantity,
        'basket_cost': basket_cost
    }
    return render(request, 'mainapp/products.html', content)


def contact(request):
    location = []
    with open(os.path.join(settings.BASE_DIR,'mainapp/templates/mainapp/contacts.json')) as read_file:
        location = json.load(read_file)
    contante = {
        'title': 'Контакты',
        'location_contacts': location
    }
    return render(request, 'mainapp/contact.html', contante)

# Create your views here.
