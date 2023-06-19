from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58),
    Curso(id=2, titulo="Algoritmos", aulas=30, horas=14),
    Curso(id=3, titulo="Lógica de Programação", aulas=42, horas=23)
]

