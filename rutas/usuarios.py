from fastapi import APIRouter, Depends
from baseModels.Usuario import Usuario
from models.Usuarios import Usuarios
from models.Typos import Typos
from .token import verificar_token

router = APIRouter(prefix="/usuario", tags=["Usuario"])

@router.get("/")
def GetUsuarios(usuario: dict = Depends(verificar_token)):
	usuarios = Usuarios.GetUsuarios()
	return usuarios

@router.post("/login")
def Autenticacion(request: Usuario):
	token = Usuarios.Autenticacion(request)
	return {"Token": token}

@router.get("/typos")
def GetTiposUsuarios(usuario: dict = Depends(verificar_token)):
	typos_usuarios = Typos.getTiposUsuarios()
	return typos_usuarios

@router.post("/")
def addTrabajador(request: Usuario, usuario: dict = Depends(verificar_token)):
	id = Usuarios.AddTrabajador(request)
	return {"id": id}

@router.put("/")
def updateTrabajador(request: Usuario, usuario: dict = Depends(verificar_token)):
	id = Usuarios.UpdateTrabajador(request)
	return {"status": "OK"}

@router.delete("/{id}")
def deleteTrabajador(id: int, usuario: dict = Depends(verificar_token)):
	id = Usuarios.DeleteTrabajador(id)
	return {"status": "OK"}