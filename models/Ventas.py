from .conexion import getConexion
from baseModels.IVenta import IVenta
from models.Typos import Typos
import uuid

class Ventas:

	__Tabla_ventas: str = "ventas"
	__Tabla_codigo_ventas: str = "codigo_ventas"
	__Tabla_tipos: str = "typo_productos"

	def __registrar_codigo_venta():
		cnn = getConexion()
		cursor = cnn.cursor()

		codigo_venta: str = str(uuid.uuid4())

		sql: str = f"INSERT INTO {Ventas.__Tabla_codigo_ventas}(codigo_venta) values(%s)"
		val: tuple = (codigo_venta,)

		cursor.execute(sql, val)
		cnn.commit()
		id_registro = cursor.lastrowid
		cursor.close()

		return id_registro

	def addVenta(venta: IVenta):
		cnn = getConexion()
		cursor = cnn.cursor()

		id_codigo_venta = Ventas.__registrar_codigo_venta()

		sql: str = f"INSERT INTO {Ventas.__Tabla_ventas}(codigo_venta, nombre, cantidad, typo, gramaje, precio_acumulado) values (%s,%s,%s,(SELECT id FROM {Ventas.__Tabla_tipos} WHERE typo = %s),%s,%s)"
		val = []

		for producto in venta['productos']:
			val.append((id_codigo_venta, producto['nombre'], producto['cantidad'], producto['typo'], producto['gramos'], producto['cantidad'] * producto['precio']))

		cursor.executemany(sql, val)
		cnn.commit()
		cursor.close()

	def getVentas(date: str):
		cnn = getConexion()
		cursor = cnn.cursor(dictionary=True)

		sql: str = """SELECT cv.codigo_venta, cv.fecha,
		    CONCAT('[', 
		        GROUP_CONCAT(
		            CONCAT(
		                '{',
		                '"nombre": "', vs.nombre, '", ',
		                '"cantidad": ', vs.cantidad, ', ',
		                '"typo": "', vs.typo, '", ',
		                '"gramaje": "', vs.gramaje, '", ',
		                '"precio_acumulado": ', vs.precio_acumulado,
		                '}'
		            )
		        SEPARATOR ','
		        ), 
		    ']') AS productos
		FROM codigo_ventas cv
		LEFT JOIN ventas vs on vs.codigo_venta = cv.id WHERE cv.fecha = %s
		"""

		val = (date,)

		cursor.execute(sql, val)
		res = cursor.fetchall()
		cursor.close()
		return res