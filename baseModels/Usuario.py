from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
	id: Optional[int] = None
	nombre: str
	typo_valor: Optional[str] = None
	typo_identificador: Optional[int] = None
	password: Optional[str] = None