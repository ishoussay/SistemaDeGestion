from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    descuento_acordado = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    plazo_pago_acordado = models.IntegerField(default=30)
    condiciones_especiales = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class OrdenCompra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden {self.id} - {self.proveedor.nombre}"

class DetalleOrdenCompra(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto} - {self.cantidad} unidades"

class HistorialNegociacion(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_negociacion = models.DateField(auto_now_add=True)
    descuento_acordado = models.DecimalField(max_digits=5, decimal_places=2)
    plazo_pago_acordado = models.IntegerField()
    condiciones_especiales = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Negociación con {self.proveedor.nombre} - {self.fecha_negociacion}"
