from .conexion import getConexion
from baseModels.IVenta import IVenta
from models.Typos import Typos
from models.Productos import Productos
from dominio.entidades.Producto import Producto
from dominio.servicios.procesar_venta import procesar_venta
import uuid

class Ventas:

	__Tabla_ventas: str = "ventas"
	__Tabla_codigo_ventas: str = "codigo_ventas"
	__Tabla_tipos: str = "typo_productos"

	def __registrar_codigo_venta(total_pago: float):
		cnn = getConexion()
		cursor = cnn.cursor()

		codigo_venta: str = str(uuid.uuid4())

		sql: str = f"INSERT INTO {Ventas.__Tabla_codigo_ventas}(codigo_venta, total_pagado) values(?, ?)"
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

		valores_actualizar_producto_contable = []
		valores_actualizar_producto_gramaje = []
		valores_insertar_venta = []

		try:

			for producto_vendido in venta_dict["productos"]:
				
				informacion_producto = Productos.getProducto(producto_vendido["id"])

				stock = 0
				cantidad_vendida = 0
				precio_acumulado = 0

				if producto_vendido["typo"] == 1:
					stock = informacion_producto["cantidad_contable"]
					cantidad_vendida = producto_vendido["cantidad"]
					producto_vendido["gramos"] = 0
					precio_acumulado = producto_vendido["cantidad"] * producto_vendido["precio"]
				else:
					stock = informacion_producto["gramaje"]
					cantidad_vendida = producto_vendido["gramos"]
					producto_vendido["cantidad"] = 0
					precio_acumulado = (producto_vendido["gramos"] * producto_vendido["precio"]) / 1000

				producto_entidad = Producto(informacion_producto["id"], informacion_producto["nombre"], stock)
				producto_procesado = procesar_venta(producto_entidad, cantidad_vendida)

				if producto_vendido["typo"] == 1:
					valores_actualizar_producto_contable.append((
						producto_procesado.total_stock,
						producto_procesado.id
					))
				elif producto_vendido["typo"] == 2:
					valores_actualizar_producto_gramaje.append((
						producto_procesado.total_stock,
						producto_procesado.id
					))

				valores_insertar_venta.append((
					producto_vendido["nombre"], 
					producto_vendido["cantidad"], 
					producto_vendido["typo"], 
					producto_vendido["gramos"], 
					precio_acumulado
				))

		except ValueError as e:
			return str(e)
		
		id_codigo_venta = Ventas.__registrar_codigo_venta(venta_dict["pago"])

		sql: str = f"INSERT INTO {Ventas.__Tabla_ventas}(codigo_venta, nombre, cantidad, typo, gramaje, precio_acumulado) values ('{id_codigo_venta}',?,?,?,?,?)"

		Productos.updateStockProductoContable(valores_actualizar_producto_contable)
		Productos.updateStockProductoGramaje(valores_actualizar_producto_gramaje)

		cursor.executemany(sql, valores_insertar_venta)
		cnn.commit()
		cursor.close()
		cnn.close()

	def getVentas(date: str):
		cnn = getConexion()
		cursor = cnn.cursor()
		sql: str = """SELECT 
			  cv.codigo_venta,
			  cv.fecha,
			  cv.total_pagado,
			  '[' || GROUP_CONCAT(
			    '{' ||
			    '"nombre": "' || vs.nombre || '", ' ||
			    '"cantidad": ' || vs.cantidad || ', ' ||
			    '"typo": "' || vs.typo || '", ' ||
			    '"gramaje": "' || vs.gramaje || '", ' ||
			    '"precio_acumulado": ' || vs.precio_acumulado ||
			    '}'
			  ) || ']' AS productos
			FROM codigo_ventas cv
			INNER JOIN ventas vs ON vs.codigo_venta = cv.id
			WHERE cv.fecha = ?
			GROUP BY cv.id, cv.codigo_venta, cv.fecha, cv.total_pagado
		"""

		val = (date,)

		cursor.execute(sql, val)
		res = cursor.fetchall()
		cursor.close()
		cnn.close()
		result = [dict(row) for row in res]
		return result