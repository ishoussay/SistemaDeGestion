class Producto:
    def __init__(self, nombre, lote, calidad_aprobada=True):
        self.nombre = nombre
        self.lote = lote
        self.calidad_aprobada = calidad_aprobada
        self.observaciones = ""

    def registrar_observaciones(self, observacion):
        """Registra observaciones sobre el control de calidad del producto."""
        self.observaciones = observacion


class ControlCalidad:
    def __init__(self):
        self.productos_inspeccionados = []

    def inspeccionar_producto(self, producto, observacion):
        """Realiza la inspección de un producto y registra las observaciones."""
        producto.registrar_observaciones(observacion)
        self.productos_inspeccionados.append(producto)

    def get_observaciones_producto(self, producto):
        """Obtiene las observaciones registradas de un producto."""
        return producto.observaciones
