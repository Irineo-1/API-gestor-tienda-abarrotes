from .conexion import getConexion
from baseModels.IVenta import IVenta
from models.Typos import Typos
import uuid

class Ventas:

	__Tabla_ventas: str = "ventas"
	__Tabla_codigo_ventas: str = "codigo_ventas"
	__Tabla_tipos: str = "typo_productos"

	def __registrar_codigo_venta(total_pago: float):
		cnn = getConexion()
		cursor = cnn.cursor()

		codigo_venta: str = str(uuid.uuid4())

		sql: str = f"INSERT INTO {Ventas.__Tabla_codigo_ventas}(codigo_venta, total_pagado) values(%s, %s)"
		val: tuple = (codigo_venta, total_pago)

		cursor.execute(sql, val)
		cnn.commit()
		id_registro = cursor.lastrowid
		cursor.close()

		return id_registro

	def addVenta(venta: IVenta):
		cnn = getConexion()
		cursor = cnn.cursor()

		venta_dict = venta.dict()

		id_codigo_venta = Ventas.__registrar_codigo_venta(venta_dict["pago"])

		sql: str = f"INSERT INTO {Ventas.__Tabla_ventas}(codigo_venta, nombre, cantidad, typo, gramaje, precio_acumulado) values (%s,%s,%s,(SELECT id FROM {Ventas.__Tabla_tipos} WHERE typo = %s),%s,%s)"
		val = []

		for producto in venta_dict["productos"]:
			val.append((
				id_codigo_venta, 
				producto["nombre"], 
				producto["cantidad"], 
				producto["typo"], 
				producto["gramos"], 
				producto["cantidad"] * producto["precio"]
			))

		print(val)
		cursor.executemany(sql, val)
		cnn.commit()
		cursor.close()

	def getVentas(date: str):
		cnn = getConexion()
		cursor = cnn.cursor(dictionary=True)

		sql: str = """SELECT cv.codigo_venta, cv.fecha, cv.total_pagado,
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
		INNER JOIN ventas vs on vs.codigo_venta = cv.id WHERE cv.fecha = %s GROUP BY cv.id, cv.codigo_venta, cv.fecha, cv.total_pagado
		"""

		val = (date,)

		cursor.execute(sql, val)
		res = cursor.fetchall()
		cursor.close()
		return res