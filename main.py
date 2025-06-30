# main.py
"""
Autor José Luis Quiroz Fabián (JLQF)

API REST básica de calculadora usando FastAPI.

Incluye operaciones de suma y factorial de un número.
"""

# main.py
from fastapi import FastAPI
from routers import calculadora_router

app = FastAPI(title="Calculadora API FastAPI",
              description="API REST para operaciones matemáticas básicas",
              version="1.0")

@app.get("/")
def inicio():
    """
    Endpoint raíz de la API.

    Returns:
        dict: Mensaje de bienvenida.
    """

    return {"mensaje": "Bienvenido a la Calculadora API"}

# Incluir rutas desde el router
app.include_router(calculadora_router.router, prefix="/calculadora", tags=["Operaciones"])


