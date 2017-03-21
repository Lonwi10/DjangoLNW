from django.contrib import admin

from .models import *


class DetallInline(admin.StackedInline):
	model = Detall

class CarritoAdmin(admin.ModelAdmin):
	inlines = [ DetallInline, ]

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(Detall)
