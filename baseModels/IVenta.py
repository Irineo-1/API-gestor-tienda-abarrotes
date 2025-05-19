from pydantic import BaseModel
from typing import List

class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    cantidad: int
    gramos: int
    typo: int

class IVenta(BaseModel):
    productos: List[Producto]
    pago: float