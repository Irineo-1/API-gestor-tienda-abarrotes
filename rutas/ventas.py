from fastapi import APIRouter
from models.Ventas import Ventas
from baseModels.IVenta import IVenta

router = APIRouter(prefix="/venta", tags=["Ventas"])

@router.get("/{date}")
def get_ventas(date: str):
    return Ventas.getVentas(date)

@router.post("/")
async def add_venta(request: IVenta):
    Ventas.addVenta(request)
    return {"response": "OK"}