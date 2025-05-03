from .conexion import getConexion

class Typos:

	__Tabla_tipos_productos: str = "typo_productos"
	__Tabla_tipos_usuarios: str = "typo_usuarios"

	def getTiposProductos():
		cnn = getConexion()
		cursor = cnn.cursor()
		cursor.execute(f"SELECT * FROM {Typos.__Tabla_tipos_productos}")
		res = cursor.fetchall()
		cursor.close()
		cnn.close()
		return res

	def getTiposUsuarios():
		cnn = getConexion()
		cursor = cnn.cursor()
		cursor.execute(f"SELECT * FROM {Typos.__Tabla_tipos_usuarios}")
		res = cursor.fetchall()
		cursor.close()
		cnn.close()
		return res