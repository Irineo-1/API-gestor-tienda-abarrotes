from .conexion import getConexion

class Productos:

    def getProductos():
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT ps.id, ps.nombre, tp.typo, ps.precio, ps.gramaje, ps.cantidad_contable FROM productos ps INNER JOIN typo_productos tp on ps.typo = tp.id")
        result = cursor.fetchall()
        cursor.close()
        return result