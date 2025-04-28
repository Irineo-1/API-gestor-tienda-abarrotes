from fastapi import APIRouter, Depends
from baseModels.IUsuario import IUsuario
from models.Usuarios import Usuarios
from .token import verificar_token

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.get("/")
def GetUsuarios(usuario: dict = Depends(verificar_token)):
	usuarios = Usuarios.GetUsuarios()
	return usuarios

@router.post("/login")
def Autenticacion(request: IUsuario):
	token = Usuarios.Autenticacion(request)
	return {"Token": token}