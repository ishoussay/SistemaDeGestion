from django.contrib import admin
from .models import Proveedor, OrdenCompra, DetalleOrdenCompra, HistorialNegociacion

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'correo')
    search_fields = ('nombre', 'correo')

@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'fecha', 'total')
    list_filter = ('proveedor',)
    search_fields = ('proveedor__nombre',)

@admin.register(DetalleOrdenCompra)
class DetalleOrdenCompraAdmin(admin.ModelAdmin):
    list_display = ('orden_compra', 'producto', 'cantidad', 'precio_unitario')

@admin.register(HistorialNegociacion)
class HistorialNegociacionAdmin(admin.ModelAdmin):
    list_display = ('proveedor', 'fecha_negociacion', 'descuento_acordado', 'plazo_pago_acordado')
    list_filter = ('proveedor',)
