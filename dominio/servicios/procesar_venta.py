from dominio.entidades.producto import Producto

def procesar_venta(producto: Producto, cantidad: int) -> Producto:
    if not producto.validarStock(cantidad):
        raise ValueError("no hay suficiente stock")
    
    producto.total_stock -= cantidad
    return producto