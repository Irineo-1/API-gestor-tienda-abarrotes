from .conexion import getConexion

class Productos:

    __Tabla_productos: str = "productos"

    def getProductos():
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(f"SELECT ps.id, ps.nombre, tp.typo, ps.precio, ps.gramaje, ps.cantidad_contable FROM {Productos.__Tabla_productos} ps INNER JOIN typo_productos tp on ps.typo = tp.id")
        result = cursor.fetchall()
        cursor.close()
        return result