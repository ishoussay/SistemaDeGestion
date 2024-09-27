from django.shortcuts import render, redirect
from .models import Proveedor, Producto, OrdenCompra, DetalleOrdenCompra

def crear_orden_compra(request):
    if request.method == 'POST':
        proveedor_id = request.POST['proveedor']
        proveedor = Proveedor.objects.get(id=proveedor_id)
        productos = request.POST.getlist('productos[]')
        cantidades = request.POST.getlist('cantidades[]')
        precios = request.POST.getlist('precios[]')

        orden = OrdenCompra.objects.create(proveedor=proveedor, estado='Pendiente', total=0)

        total_orden = 0
        for i in range(len(productos)):
            producto = Producto.objects.get(id=productos[i])
            cantidad = int(cantidades[i])
            precio = float(precios[i])
            DetalleOrdenCompra.objects.create(orden=orden, producto=producto, cantidad=cantidad, precio=precio)
            subtotal_con_descuento = (cantidad * precio) * (1 - proveedor.descuento / 100)
            total_orden += subtotal_con_descuento

        orden.total = total_orden
        orden.save()

        return redirect('orden_compra_detalle', orden_id=orden.id)

    else:
        proveedores = Proveedor.objects.all()
        productos = Producto.objects.all()
        return render(request, 'compras/crear_orden_compra.html', {'proveedores': proveedores, 'productos': productos})
