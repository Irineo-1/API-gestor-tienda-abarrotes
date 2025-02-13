from fastapi import APIRouter, Depends
from baseModels.IUsuario import IUsuario
from models.Usuarios import Usuarios
from .token import verificar_token

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.post("/login")
def Autenticacion(request: IUsuario):
	token = Usuarios.Autenticacion(request)
	return {"Token": token}