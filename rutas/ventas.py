from fastapi import APIRouter, Depends
from models.Ventas import Ventas
from baseModels.IVenta import IVenta
from .token import verificar_token

router = APIRouter(prefix="/venta", tags=["Ventas"])

@router.get("/{date}")
def get_ventas(date: str, usuario: dict = Depends(verificar_token)):
    return Ventas.getVentas(date)

@router.post("/")
async def add_venta(request: IVenta, usuario: dict = Depends(verificar_token)):
    Ventas.addVenta(request)
    return {"response": "OK"}