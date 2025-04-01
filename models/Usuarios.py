from .conexion import getConexion
from rutas.token import generar_token
from baseModels.IUsuario import IUsuario

class Usuarios: 

	def Autenticacion(request: IUsuario):
		return generar_token(request.usuario)