from .conexion import getConexion

class Typos:

	__Tabla_tipos: str = "typo_productos"

	def getTiposProductos():
		cnn = getConexion()
		cursor = cnn.cursor()
		cursor.execute(f"SELECT * FROM {Typos.__Tabla_tipos}")
		res = cursor.fetchall()
		cursor.close()
		cnn.close()
		return res

	def getTiposUsuarios():
		cnn = getConexion()
		cursor = cnn.cursor()
		cursor.execute(f"SELECT * FROM {Typos.__Tabla_tipos}")
		res = cursor.fetchall()
		cursor.close()
		cnn.close()
		return res