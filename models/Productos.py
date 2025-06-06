from .conexion import getConexion
from baseModels.IProducto import IProducto

class Productos:

    __Tabla_productos: str = "productos"

    def getProductos():
        cnn = getConexion()
        cursor = cnn.cursor()
        sql: str = f"SELECT id, nombre, typo, precio, gramaje, cantidad_contable, codigo_barras FROM {Productos.__Tabla_productos} WHERE cantidad_contable > 0 OR gramaje > 0"
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        cnn.close()
        return result

    def getProducto(id: int):
        cnn = getConexion()
        cursor = cnn.cursor()
        sql: str = f"SELECT id, nombre, precio, gramaje, cantidad_contable, codigo_barras FROM {Productos.__Tabla_productos} WHERE id = ?"
        val = (id,)
        cursor.execute(sql, val)
        result = cursor.fetchone()
        cursor.close()
        cnn.close()
        return result
    
    def addProducto(producto: IProducto):
        cnn = getConexion()
        cursor = cnn.cursor()
        sql: str = f"INSERT INTO {Productos.__Tabla_productos} (codigo_barras, nombre, typo, precio, gramaje, cantidad_contable) VALUES(?,?,?,?,?,?)"
        val = (producto.codigo_barras, producto.nombre, producto.typo, producto.precio, producto.gramaje, producto.cantidad_contable)
        cursor.execute(sql, val)
        cnn.commit()
        id = cursor.lastrowid
        cursor.close()
        cnn.close()
        return id


    def deleteProducto(id: int):
        cnn = getConexion()
        cursor = cnn.cursor()
        sql: str = f"DELETE FROM {Productos.__Tabla_productos} WHERE id = ?"
        val = (id,)
        cursor.execute(sql, val)
        cnn.commit()
        cursor.close()
        cnn.close()


    def updateProducto(producto: IProducto):
        cnn = getConexion()
        cursor = cnn.cursor()
        sql: str = f"UPDATE {Productos.__Tabla_productos} SET nombre = ?, precio = ?, gramaje = ?, cantidad_contable = ? WHERE id = ?"
        val = (producto.nombre, producto.precio, producto.gramaje, producto.cantidad_contable, producto.id)
        cursor.execute(sql, val)
        cnn.commit()
        cursor.close()
        cnn.close()

    def updateStockProductoContable(productos_vendidos: list):
        cnn = getConexion()
        cursor = cnn.cursor()

        sql: str = f"UPDATE {Productos.__Tabla_productos} SET cantidad_contable = ? WHERE id = ?"
        
        cursor.executemany(sql, productos_vendidos)
        cnn.commit()
        cursor.close()
        cnn.close()

    def updateStockProductoGramaje(productos_vendidos: list):
        cnn = getConexion()
        cursor = cnn.cursor()

        sql: str = f"UPDATE {Productos.__Tabla_productos} SET gramaje = ? WHERE id = ?"
        
        cursor.executemany(sql, productos_vendidos)
        cnn.commit()
        cursor.close()
        cnn.close()