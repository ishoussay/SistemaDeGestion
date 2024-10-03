Feature: Registro de facturas

  Como un empleado del área de compras
  Quiero ingresar los detalles de una factura
  Para asegurarme de que esté registrada correctamente para su posterior pago

  Scenario: Registrar una factura correctamente
    Given un proveedor llamado "Proveedor X" y una fecha "2024-09-13"
    When ingreso los detalles de la factura con total "5000"
    Then la factura debe ser registrada correctamente en el sistema
