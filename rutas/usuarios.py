from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
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
	try:
		datos_usuario = Usuarios.Autenticacion(request)
		return JSONResponse(status_code=200, content=datos_usuario)
	except ValueError as error:
		return JSONResponse(status_code=401, content={"error": str(error)})

@router.get("/typos")
def GetTiposUsuarios(usuario: dict = Depends(verificar_token)):
	typos_usuarios = Typos.getTiposUsuarios()
	return typos_usuarios

@router.post("/")
def addTrabajador(request: Usuario, usuario: dict = Depends(verificar_token)):
	id = Usuarios.AddTrabajador(request)
	return JSONResponse(status_code=200, content={"id": id})

@router.put("/")
def updateTrabajador(request: Usuario, usuario: dict = Depends(verificar_token)):
	id = Usuarios.UpdateTrabajador(request)
	return Response(status_code=204)

@router.delete("/{id}")
def deleteTrabajador(id: int, usuario: dict = Depends(verificar_token)):
	id = Usuarios.DeleteTrabajador(id)
	return Response(status_code=204)