from fastapi import Query
from fastapi import Header
from typing import Optional, Any, Dict, List
from fastapi import APIRouter

api_router = APIRouter()

@api_router.get('/calculadora')
async def calculo(
    a: int = Query(default=None, gt=5), 
    b: int = Query(default=None, lt=10), 
    c: Optional[int] = 0,
    x_geek: str = Header(default=None)
):
    soma = a + b + c
    print(f'X_GEEK: {x_geek}')
    return {"resultado" : soma}
