from pydantic import BaseModel
from typing import List

class Producto(BaseModel):
    nombre: str
    precio: float
    cantidad: int
    gramos: int
    typo: str

class IVenta(BaseModel):
    productos: List[Producto]
    pago: float