class Factura:
    def __init__(self, proveedor, fecha, total):
        self.proveedor = proveedor
        self.fecha = fecha
        self.total = total

    def registrar(self):
 # Aquí iría la lógica para registrar la factura
        return f"Factura registrada: {self.proveedor},Fecha: {self.fecha}, Total: {self.total}"
from behave import given, when, then
from factura_system import Factura    

@given('un proveedor llamado "{proveedor}" y una fecha "{fecha}"')
def step_given_proveedor_y_fecha(context, proveedor, fecha):
    context.proveedor = proveedor
    context.fecha = fecha

@when('ingreso los detalles de la factura con total "{total}"')
def step_when_ingreso_detalles(context, total):
    context.total = total
    context.factura = Factura(context.proveedor, context.fecha, context.total)

@then('la factura debe ser registrada correctamente en el sistema')
def step_then_factura_registrada(context):
    resultado = context.factura.registrar()
    assert "Factura registrada" in resultado, "La factura no se registró correctamente"
    print(resultado)
