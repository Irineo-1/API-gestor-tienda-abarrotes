from .conexion import getConexion

class Typos:

	def getTiposProductos():
		cnn = getConexion()
		cursor = cnn.cursor(dictionary=True)
		cursor.execute("SELECT * FROM typo_productos")
		res = cursor.fetchall()
		cursor.close()
		return res

	def getTiposUsuarios():
		cnn = getConexion()
		cursor = cnn.cursor(dictionary=True)
		cursor.execute("SELECT * FROM typo_usuarios")
		res = cursor.fetchall()
		cursor.close()
		return res