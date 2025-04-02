from pydantic import BaseModel

class IProducto(BaseModel):
	id: int
	codigo_barras: str
	nombre: str
	precio: float
	gramaje: float
	cantidad_contable: int
	typo: int