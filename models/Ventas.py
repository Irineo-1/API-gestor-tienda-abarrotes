from .conexion import getConexion
from baseModels.IVenta import IVenta
from models.Typos import Typos
import uuid

class Ventas:

	def addVenta(venta: IVenta):

		# get typos productos
		cnn = getConexion()
		cursor = cnn.cursor(dictionary=True)
		codigo_venta: str = uuid.uuid4()
		sql: str = "INSERT INTO ventas(codigo_venta, nombre, cantidad, typo, gramaje, precio_acumulado) values "
		cada_producto: str = ""

		for producto in venta['productos']:
			cada_producto += f"""(
			'{codigo_venta}', 
			'{producto['nombre']}', 
			{producto['cantidad']}, 
			(SELECT id FROM typo_productos WHERE typo = '{producto['typo']}'), 
			{producto['gramos']}, 
			{producto['cantidad'] * producto['precio']}),"""

		sql = sql + cada_producto[0:len(cada_producto) -1]
		print(sql)
		cursor.execute(sql)
		cnn.commit()
		cursor.close()