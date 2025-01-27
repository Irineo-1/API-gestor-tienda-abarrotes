from .conexion import getConexion
from baseModels.IProducto import IProducto

class Productos:

    __Tabla_productos: str = "productos"

    def getProductos():
        conexion = getConexion()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(f"SELECT ps.id, ps.nombre, tp.typo, ps.precio, ps.gramaje, ps.cantidad_contable, ps.codigo_barras FROM {Productos.__Tabla_productos} ps INNER JOIN typo_productos tp on ps.typo = tp.id")
        result = cursor.fetchall()
        cursor.close()
        return result


    def addProducto(producto: IProducto):
        conexion = getConexion()
        cursor = conexion.cursor()
        sql: str = f"INSERT INTO {Productos.__Tabla_productos} (codigo_barras, nombre, typo, precio, gramaje, cantidad_contable) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (producto.codigo_barras, producto.nombre, producto.typo, producto.precio, producto.gramaje, producto.cantidad_contable)
        cursor.execute(sql, val)
        conexion.commit()
        id = cursor.lastrowid
        cursor.close()
        return id


    def deleteProducto(id: int):
        conexion = getConexion()
        cursor = conexion.cursor()
        sql: str = f"DELETE FROM {Productos.__Tabla_productos} WHERE id = %s"
        val = (id,)
        cursor.execute(sql, val)
        conexion.commit()
        cursor.close()


    def updateProducto(producto: IProducto):
        conexion = getConexion()
        cursor = conexion.cursor()
        sql: str = f"UPDATE {Productos.__Tabla_productos} SET nombre = %s, precio = %s, gramaje = %s, cantidad_contable = %s WHERE id = %s"
        val = (producto.nombre, producto.precio, producto.gramaje, producto.cantidad_contable, producto.id)
        cursor.execute(sql, val)
        conexion.commit()
        cursor.close()