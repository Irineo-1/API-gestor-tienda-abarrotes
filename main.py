from typing import Union
from fastapi import FastAPI
from models.Productos import Productos
from models.Ventas import Ventas
from fastapi.middleware.cors import CORSMiddleware
from baseModels.IVenta import IVenta
from baseModels.IProducto import IProducto
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

@app.post("/productos")
def addProducto(producto: IProducto):
    id = Productos.addProducto(producto)
    return {"id": id}

@app.put("/productos")
def updateProducto(producto: IProducto):
    Productos.updateProducto(producto)
    return {"response": "ok"}

@app.delete("/productos/{id}")
def deleteProducto(id: int):
    Productos.deleteProducto(id)
    return {"message": "Producto eliminado"}

@app.get("/venta/{date}")
def getVentas(date: str):
    res = Ventas.getVentas(date)
    return res

@app.post("/venta")
async def addVenta(request: IVenta):
    Ventas.addVenta(request)
    return {"response": "OK"}