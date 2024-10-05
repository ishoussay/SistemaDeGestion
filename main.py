from recepcionar_mercancia import Producto, ControlCalidad

def main():
    control_calidad = ControlCalidad()

    while True:
        print("\n--- Control de Calidad ---")
        nombre = input("Ingrese el nombre del producto: ")
        lote = input("Ingrese el lote del producto: ")
        observacion = input("Ingrese las observaciones del producto: ")

        producto = Producto(nombre, lote)
        control_calidad.inspeccionar_producto(producto, observacion)

        continuar = input("¿Desea inspeccionar otro producto? (s/n): ")
        if continuar.lower() != 's':
            break

    print("\nResultados de la inspección:")
    for producto in control_calidad.productos_inspeccionados:
        print(f"- Producto: {producto.nombre}, Lote: {producto.lote}, Observaciones: {producto.observaciones}")

if __name__ == "__main__":
    main()
