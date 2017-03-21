from django.conf.urls import url

from . import views
from views import add
from views import cerrar

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<id>[0-9]+)$', views.product, name='product'),
    url(r'^add/(?P<producte_id>[0-9]+)', add ),
    url(r'^listacarritos', views.listacarritos, name='carrito_list'),
    url(r'^carrito/(?P<id>[0-9]+)$', views.carrito, name='carro'),
    url(r'^cerrar', cerrar),
    url(r'^reabrir/(?P<id>[0-9]+)', views.reabrir)
]
