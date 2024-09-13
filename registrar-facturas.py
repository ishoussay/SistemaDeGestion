#COMO (provedor-comprador)
#QUIERO (ingresar los detalles de una factura fecha y total)
#PARA (asegurarme de que la factura esté registrada correctamente para su posterior pago).


"""
Dado que estoy en el formulario de registro de facturas,
Cuando ingreso todos los detalles de la factura y adjunto los documentos necesarios,
Entonces el sistema debe confirmar el registro exitoso con un número de referencia único y notificarme sobre el estado de la factura, ya sea aceptada, rechazada o si requiere correcciones.
Dado que estoy en la sección de facturas del sistema,
Cuando accedo a la lista de facturas registradas,
Entonces debo ver un resumen de cada factura, incluyendo el número de factura, el proveedor, la fecha y el monto total, y tener la opción de visualizar los detalles completos.
"""

# factura_system.py

class FacturaSystem:
    def __init__(self):
        self.facturas = {}
        self.next_id = 1

    def registrar_factura(self, proveedor, fecha, monto_total, descripcion, documentos=None):
        factura_id = self.next_id
        self.next_id += 1
        self.facturas[factura_id] = {
            "proveedor": proveedor,
            "fecha": fecha,
            "monto_total": monto_total,
            "descripcion": descripcion,
            "documentos": documentos or [],
            "estado": "pendiente"
        }
        return factura_id

    def actualizar_estado_factura(self, factura_id, estado):
        if factura_id in self.facturas:
            self.facturas[factura_id]["estado"] = estado
            return True
        return False

    def obtener_factura(self, factura_id):
        return self.facturas.get(factura_id, None)

    def obtener_resumen_facturas(self):
        return [
            {
                "factura_id": fid,
                "proveedor": f["proveedor"],
                "fecha": f["fecha"],
                "monto_total": f["monto_total"],
                "estado": f["estado"]
            }
            for fid, f in self.facturas.items()
        ]
