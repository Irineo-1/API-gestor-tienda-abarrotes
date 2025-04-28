from .conexion import getConexion
from rutas.token import generar_token
from baseModels.IUsuario import IUsuario

class Usuarios: 

	__Tabla_usuarios: str = "usuarios"
	__Tabla_typo_usuarios: str = "typo_usuarios"

	def Autenticacion(request: IUsuario):
		return generar_token(request.usuario)

	def GetUsuarios():
		cnn = getConexion()
		cursor = cnn.cursor(dictionary=True)
		sql: str = f"""
			SELECT user.id, user.usuario, typouser.typo FROM {Usuarios.__Tabla_usuarios} user 
			INNER JOIN {Usuarios.__Tabla_typo_usuarios} typouser 
			on typouser.id = user.typo
		"""
		cursor.execute(sql)
		res = cursor.fetchall()
		cursor.close()
		return res