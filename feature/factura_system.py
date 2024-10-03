# factura_system.py

class Factura:
    def __init__(self, proveedor, fecha, total):
        self.proveedor = proveedor
        self.fecha = fecha
        self.total = total

    def registrar(self):
        # Aquí iría la lógica para registrar la factura
        return f"Factura registrada: {self.proveedor}, Fecha: {self.fecha}, Total: {self.total}"
