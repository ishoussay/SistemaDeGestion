from django.shortcuts import render, redirect
from .models import Proveedor, OrdenCompra, DetalleOrdenCompra, HistorialNegociacion

# Vista para solicitar una orden de compra
def crear_orden_compra(request):
    proveedores = Proveedor.objects.all()

    if request.method == 'POST':
        proveedor_id = request.POST['proveedor']
        proveedor = Proveedor.objects.get(id=proveedor_id)
        orden = OrdenCompra.objects.create(proveedor=proveedor, total=0)
        
        productos = request.POST.getlist('producto[]')
        cantidades = request.POST.getlist('cantidad[]')
        precios = request.POST.getlist('precio[]')

        total = 0
        for producto, cantidad, precio in zip(productos, cantidades, precios):
            cantidad = int(cantidad)
            precio = float(precio)
            total += cantidad * precio
            DetalleOrdenCompra.objects.create(
                orden_compra=orden,
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio
            )
        
        orden.total = total
        orden.save()

        return redirect('lista_ordenes_compra')

    return render(request, 'compras/crear_orden_compra.html', {'proveedores': proveedores})

# Vista para negociar con un proveedor
def negociar_con_proveedor(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)

    if request.method == 'POST':
        descuento_acordado = float(request.POST['descuento_acordado'])
        plazo_pago_acordado = int(request.POST['plazo_pago_acordado'])
        condiciones_especiales = request.POST['condiciones_especiales']
        observaciones = request.POST['observaciones']

        # Actualizar proveedor
        proveedor.descuento_acordado = descuento_acordado
        proveedor.plazo_pago_acordado = plazo_pago_acordado
        proveedor.condiciones_especiales = condiciones_especiales
        proveedor.save()

        # Registrar la negociación
        HistorialNegociacion.objects.create(
            proveedor=proveedor,
            descuento_acordado=descuento_acordado,
            plazo_pago_acordado=plazo_pago_acordado,
            condiciones_especiales=condiciones_especiales,
            observaciones=observaciones
        )

        return redirect('historial_negociaciones', proveedor_id=proveedor.id)

    return render(request, 'compras/negociar_proveedor.html', {'proveedor': proveedor})

# Vista para mostrar el historial de negociaciones
def historial_negociaciones(request, proveedor_id):
    proveedor = Proveedor.objects.get(id=proveedor_id)
    negociaciones = HistorialNegociacion.objects.filter(proveedor=proveedor).order_by('-fecha_negociacion')
    return render(request, 'compras/historial_negociaciones.html', {'proveedor': proveedor, 'negociaciones': negociaciones})
