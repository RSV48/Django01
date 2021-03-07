import json
import os

from django.conf import settings
from django.shortcuts import render


def main(request):
    contante = {
        'title': 'Главная',
    }
    return render(request, 'mainapp/index.html', contante)


def products(request):
    links_menu = [
        {'href': 'products_all', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'класика'},
    ]
    contante = {
        'title': 'Продукты',
        'links_menu': links_menu
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
