from .conexion import getConexion
from rutas.token import generar_token
from baseModels.Usuario import Usuario
from .cifrado.password_encrypt import hash_password

class Usuarios: 

	__Tabla_usuarios: str = "usuarios"
	__Tabla_typo_usuarios: str = "typo_usuarios"

	def Autenticacion(request: Usuario):
		return generar_token(request.usuario)

	def GetUsuarios():
		cnn = getConexion()
		cursor = cnn.cursor()
		sql: str = f"""
			SELECT user.id, user.usuario, typouser.typo FROM {Usuarios.__Tabla_usuarios} user 
			INNER JOIN {Usuarios.__Tabla_typo_usuarios} typouser 
			on typouser.id = user.typo
		"""
		cursor.execute(sql)
		res = cursor.fetchall()
		cursor.close()
		cnn.close()
		return res

	def AddTrabajador(request: Usuario):
		cnn = getConexion()
		cursor = cnn.cursor()
		sql: str = f"INSERT INTO {Usuarios.__Tabla_usuarios} (usuario, typo, password) VALUES(?,?,?)"

		# tratamiento para la contraneña
		encode_password = hash_password(request.password)

		val = (request.usuario, request.typo, encode_password)

		cursor.execute(sql, val)
		cnn.commit()
		cursor.close()
		cnn.close()