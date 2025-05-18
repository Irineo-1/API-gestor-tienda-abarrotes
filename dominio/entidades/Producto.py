class Producto:
    
    def __init__(self, total_stock: int):
        self.total_stock = total_stock

    def validarStock(self, cantidad: int) -> bool:
        return self.total_stock > cantidad