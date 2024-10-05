def crear_producto(nombre, lote):
    """Crea un nuevo producto como un diccionario."""
    return {
        'nombre': nombre,
        'lote': lote,
        'observaciones': ""
    }

def registrar_observaciones(producto, observacion):
    """Registra observaciones sobre el control de calidad del producto."""
    producto['observaciones'] = observacion

def inspeccionar_producto(control_calidad, producto, observacion):
    """Realiza la inspección de un producto y registra las observaciones."""
    registrar_observaciones(producto, observacion)
    control_calidad.append(producto)

def mostrar_productos_inspeccionados(control_calidad):
    """Muestra todos los productos inspeccionados."""
    print("\nProductos inspeccionados:")
    for producto in control_calidad:
        print(f"- Nombre: {producto['nombre']}, Lote: {producto['lote']}, Observaciones: {producto['observaciones']}")
