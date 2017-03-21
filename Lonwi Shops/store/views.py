from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect

from .models import *
from .models import Product, Carrito, Detall, Category
from django.views.generic.list import ListView



def index(request):
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def product(request, id):
    template = loader.get_template('product.html')
    context = {
        'product': Product.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))

def listacarritos(request):
    template = loader.get_template('listacarritos.html')
    context = {
        'carrito_list': Carrito.objects.all()
    }
    return HttpResponse(template.render(context, request))

def carrito(request, id):
    template = loader.get_template('carrito.html')
    carro = Carrito.objects.get(id=id)
    context = {
        'detalls': Detall.objects.filter(carrito=carro)
    }
    return HttpResponse(template.render(context, request))
    
def cerrar(request):
    carro= Carrito.objects.filter(obert=True)[0]
    carro.obert=False
    carro.save()

    return redirect('/')

def reabrir(request, id):
    compr = Carrito.objects.filter(obert=True).count()
    if ( compr ):
        carro= Carrito.objects.filter(obert=True).first()
        carro.obert=False
        carro.save()

    carro = Carrito.objects.filter(id=id).first()
    carro.obert=True
    carro.save()

    return redirect('/')


def add(request, producte_id):
    carro = Carrito.objects.filter(obert=True).count()
    contCarros = Carrito.objects.count()
    num = contCarros + 1
    if( carro ):
        # si hi ha carro obert, l'omplo
        carro = Carrito.objects.filter(obert=True)[0]
    else:
        # si no, el creo
        carro = Carrito()
        carro.nom = "Prova "+ str(num)
        carro.save()

    detall = Detall()
    detall.carrito = carro
    detall.producte = Product.objects.get(pk=producte_id)
    detall.quantitat = 1
    detall.save()

    return redirect('/')

