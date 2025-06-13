from typing import Optional
from pydantic import BaseModel

# posible desuso
# class IUsuario(BaseModel): 
# 	usuario: str
# 	password: str


class Usuario(BaseModel):
	id: Optional[int] = None
	usuario: str
	typo_valor: Optional[str] = None
	typo_identificador: Optional[int] = None
	password: Optional[str] = None