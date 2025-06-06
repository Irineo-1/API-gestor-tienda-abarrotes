from dominio.entidades.Producto import Producto

def procesar_venta(producto: Producto, cantidad: int) -> Producto:
    if not producto.validarStock(cantidad):
        raise ValueError("no hay suficiente producto de " + producto.nombre)
    
    producto.total_stock -= cantidad
    return producto