function agregarProducto() {
    var productosDiv = document.getElementById('productos');
    var nuevoProducto = document.createElement('div');
    nuevoProducto.className = 'producto';
    nuevoProducto.innerHTML = `
      <label>Producto:</label>
      <input type="text" name="producto[]" required>
      
      <label>Cantidad:</label>
      <input type="number" name="cantidad[]" min="1" required>
      
      <label>Precio Unitario:</label>
      <input type="number" step="0.01" name="precio[]" required>
      <button type="button" onclick="removerProducto(this)">Eliminar</button>
    `;
    productosDiv.appendChild(nuevoProducto);
}

function removerProducto(boton) {
    var productoDiv = boton.parentElement;
    productoDiv.remove();
}
