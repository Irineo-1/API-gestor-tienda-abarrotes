from fastapi import APIRouter, Depends
from models.Productos import Productos
from baseModels.IProducto import IProducto
from .token import verificar_token

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def get_productos(usuario: dict = Depends(verificar_token)):
    return Productos.getProductos()

@router.post("/")
def add_producto(producto: IProducto, usuario: dict = Depends(verificar_token)):
    id = Productos.addProducto(producto)
    return {"id": id}

@router.put("/")
def update_producto(producto: IProducto, usuario: dict = Depends(verificar_token)):
    Productos.updateProducto(producto)
    return {"response": "ok"}

@router.delete("/{id}")
def delete_producto(id: int, usuario: dict = Depends(verificar_token)):
    Productos.deleteProducto(id)
    return {"message": "Producto eliminado"}