from typing import Union
from fastapi import FastAPI
from models.Productos import Productos
from models.Ventas import Ventas
from fastapi.middleware.cors import CORSMiddleware
from baseModels.IVenta import IVenta
from fastapi import Request

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/productos")
def getProductos():
    productos = Productos.getProductos()
    return productos

# @app.get("/productos/{id}")
# def getProducto(id: int):
#     # producto = Productos.getProducto(id)
#     return {"id": id, "nombre": "Producto 1", "precio": 100.0}

# @app.post("/productos")
# def addProducto(request: Request):
#     # producto = Productos.addProducto(producto)
#     return producto

# @app.put("/productos/{id}")
# def updateProducto(id: int, producto: dict):
#     # producto = Productos.updateProducto(id, producto)
#     return producto

# @app.delete("/productos/{id}")
# def deleteProducto(id: int):
#     # producto = Productos.deleteProducto(id)
#     return {"message": "Producto eliminado"}

@app.get("/venta/{date}")
def getVentas(date: str):
    res = Ventas.getVentas(date)
    return res

@app.post("/venta")
async def addVenta(request: IVenta):
    Ventas.addVenta(request)
    return {"response": "OK"}