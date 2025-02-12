from fastapi import APIRouter
from baseModels.IUsuario import IUsuario
from models.Usuarios import Usuarios

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.post("/login")
def Autenticacion(request: IUsuario):
	token = Usuarios.Autenticacion(request)
	return {"Token": token}