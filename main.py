from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rutas.productos import router as productos_router
from rutas.ventas import router as ventas_router
from rutas.usuarios import router as usuarios_router

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

app.include_router(productos_router)
app.include_router(ventas_router)
app.include_router(usuarios_router)