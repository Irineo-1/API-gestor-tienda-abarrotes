class Producto:
    
    def __init__(self, id: int, nombre: str, total_stock: int):
        self.id = id
        self.nombre = nombre
        self.total_stock = total_stock

    def validarStock(self, cantidad: int) -> bool:
        return self.total_stock > cantidad