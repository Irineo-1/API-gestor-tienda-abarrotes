from .conexion import getConexion
from rutas.token import generar_token
from baseModels.Usuario import Usuario
from .cifrado.password_encrypt import hash_password, verify_password

class Usuarios: 

	__Tabla_usuarios: str = "usuarios"
	__Tabla_typo_usuarios: str = "typo_usuarios"

	def Autenticacion(usuario: Usuario):
		cnn = getConexion()
		cursor = cnn.cursor()

		sql = f"""
			SELECT user.id, user.nombre, user.typo as typo_identificador, user.password, typouser.typo as typo_valor FROM {Usuarios.__Tabla_usuarios} user
			INNER JOIN {Usuarios.__Tabla_typo_usuarios} typouser on typouser.id = user.typo
		 	WHERE nombre = ?
		"""

		valores = (usuario.nombre,)

		cursor.execute(sql, valores)
		usuario_consultado = cursor.fetchone()

		if not usuario_consultado:
			raise ValueError("Usuario incorrecto")

		cursor.close()
		cnn.close()

		if verify_password(usuario.password, usuario_consultado["password"]):
			return {
				"usuario": {
					"id": usuario_consultado["id"],
					"nombre": usuario_consultado["nombre"],
					"typo_valor": usuario_consultado["typo_valor"],
					"typo_identificador": usuario_consultado["typo_identificador"],
				},
				"Token": generar_token(usuario.nombre)
			}
		else:
			raise ValueError("contraseña incorrecta")

	def GetUsuarios():
		cnn = getConexion()
		cursor = cnn.cursor()
		sql: str = f"""
			SELECT user.id, user.nombre, typouser.typo as typo_valor, typouser.id as typo_identificador FROM {Usuarios.__Tabla_usuarios} user 
			INNER JOIN {Usuarios.__Tabla_typo_usuarios} typouser 
			on typouser.id = user.typo
		"""
		cursor.execute(sql)
		res = cursor.fetchall()
		cursor.close()
		cnn.close()
		return res

	def AddTrabajador(usuario: Usuario):
		cnn = getConexion()
		cursor = cnn.cursor()
		sql: str = f"INSERT INTO {Usuarios.__Tabla_usuarios} (nombre, typo, password) VALUES(?,?,?)"

		# tratamiento para la contraneña
		encode_password = hash_password(usuario.password)

		val = (usuario.nombre, usuario.typo_identificador, encode_password)

		cursor.execute(sql, val)
		cnn.commit()
		id = cursor.lastrowid
		cursor.close()
		cnn.close()
		return id

	def UpdateTrabajador(usuario: Usuario):
		cnn = getConexion()
		cursor = cnn.cursor()

		encode_password = hash_password(usuario.password)

		sql: str = f"UPDATE {Usuarios.__Tabla_usuarios} SET nombre = ?, password = ? WHERE id = ?"

		val = (usuario.nombre, encode_password, usuario.id)

		cursor.execute(sql, val)
		cnn.commit()
		cursor.close()
		cnn.close()

	def DeleteTrabajador(id: int):
		cnn = getConexion()
		cursor = cnn.cursor()
		sql: str = f"DELETE FROM {Usuarios.__Tabla_usuarios} WHERE id = ?"

		val = (id,)

		cursor.execute(sql, val)
		cnn.commit()
		cursor.close()
		cnn.close()