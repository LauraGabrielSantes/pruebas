"""
Router de operaciones matemáticas para la API de calculadora.
"""

from fastapi import APIRouter
from models.request_models import SumaRequest
from services.operaciones_service import sumar, factorial

router = APIRouter()

@router.post("/suma")
def ruta_suma(datos: SumaRequest):
    """
    Calcula la suma de dos números.

    Args:
        datos (SumaRequest): Cuerpo de la petición con dos números.

    Returns:
        dict: Resultado de la suma.
    """

    resultado = sumar(datos.a, datos.b)
    return {"resultado": resultado}

@router.get("/factorial/{n}")
def ruta_factorial(n: int):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n (int): Número entero no negativo.

    Returns:
        dict: Resultado del factorial.

    Raises:
        HTTPException: Si el número es negativo.
    """
    resultado = factorial(n)
    return {"resultado": resultado}
