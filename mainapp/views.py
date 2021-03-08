import json
import os

from django.conf import settings
from django.shortcuts import render

from mainapp.models import Product, ProductCategory



def main(request):
    products = Product.objects.all()[:4]
    contante = {
        'title': 'Главная',
        'products':products
    }
    return render(request, 'mainapp/index.html', contante)


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    same_products = Product.objects.all()[:3]
    contante = {
        'title': 'Продукты',
        'links_menu': links_menu,
        'same_products':same_products
    }
    return render(request, 'mainapp/products.html', contante)


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
