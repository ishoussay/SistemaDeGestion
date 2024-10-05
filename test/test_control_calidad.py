import unittest
from recepcionar_mercancia import Producto, ControlCalidad
class TestControlCalidad(unittest.TestCase):

    def test_registro_observaciones(self):
        # Dado que los productos están siendo inspeccionados
        producto = Producto("Galletas", "Lote001")
        control_calidad = ControlCalidad()
        
        # Cuando el encargado realiza observaciones sobre la calidad del producto
        observacion = "Paquete dañado"
        control_calidad.inspeccionar_producto(producto, observacion)
        
        # Entonces el sistema debe registrar las observaciones en el perfil del producto
        self.assertEqual(producto.observaciones, "Paquete dañado")
    
    def test_producto_sin_observaciones_inicialmente(self):
        # Dado un producto recién creado
        producto = Producto("Caramelos", "Lote002")
        
        # Entonces debe tener observaciones vacías por defecto
        self.assertEqual(producto.observaciones, "")
    
    def test_inspeccionar_varios_productos(self):
        # Dado varios productos que están siendo inspeccionados
        producto1 = Producto("Galletas", "Lote001")
        producto2 = Producto("Caramelos", "Lote002")
        control_calidad = ControlCalidad()
        
        # Cuando el encargado inspecciona varios productos
        control_calidad.inspeccionar_producto(producto1, "Paquete dañado")
        control_calidad.inspeccionar_producto(producto2, "Producto vencido")
        
        # Entonces el sistema debe registrar las observaciones correctas para cada uno
        self.assertEqual(producto1.observaciones, "Paquete dañado")
        self.assertEqual(producto2.observaciones, "Producto vencido")

if __name__ == '__main__':
    unittest.main()
