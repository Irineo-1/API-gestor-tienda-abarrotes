from fastapi import APIRouter, Depends
from models.Ventas import Ventas
from baseModels.IVenta import IVenta
from fastapi.responses import JSONResponse, Response
from .token import verificar_token

router = APIRouter(prefix="/venta", tags=["Ventas"])

@router.get("/{date}")
def get_ventas(date: str, usuario: dict = Depends(verificar_token)):
    return JSONResponse(status_code=200, content=Ventas.getVentas(date))

@router.post("/")
async def add_venta(request: IVenta, usuario: dict = Depends(verificar_token)):
    error = Ventas.addVenta(request)
    if error:
        return JSONResponse(status_code=406, content={"error": error})
    return Response(status_code=200)