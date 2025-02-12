from pydantic import BaseModel

class IUsuario(BaseModel):
	usuario: str
	password: str