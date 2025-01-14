from pydantic import BaseModel

class IVenta(BaseModel):
    productos: dict
    precio: float