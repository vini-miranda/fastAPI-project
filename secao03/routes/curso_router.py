from typing import Optional, Any, Dict, List
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Depends
from fastapi import APIRouter
from models import Curso
from models import cursos
from time import sleep

api_router = APIRouter()

def db_simulator():
    try:
        print("Abrindo conexão com banco de dados...")
        sleep(1)
    finally:
        print("fechando conexão com banco de dados...")
        sleep(1)

@api_router.get('/cursos', 
         description="Retorna lista de cursos", 
         summary="Retorna todos os cursos",
         response_model=List[Curso])
async def get_cursos(db: Any = Depends(db_simulator)):
    return cursos

@api_router.get('/cursos/{curso_id}',
                description="Retorna um curso da lista", 
                summary="Retorna um curso",
                response_model=Curso)
async def get_curso(curso_id: int, db: Any = Depends(db_simulator)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")    

@api_router.post('/cursos', 
          status_code=status.HTTP_201_CREATED,
          description="Insere um novo curso", 
          summary="Posta curso",
          response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(db_simulator)):
    next_id: int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso

@api_router.put('/cursos',
                description="Edita um curso da lista", 
                summary="Edita um curso")
async def put_curso(curso: Curso, db: Any = Depends(db_simulator)):
    if cursos[curso.id - 1] != None:
        cursos[curso.id - 1] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@api_router.delete('/cursos/{curso_id}',
                   description="Deleta um curso da lista", 
                   summary="Deleta um curso")
async def delete_curso(curso_id: int, db: Any = Depends(db_simulator)):
    if cursos[curso_id -1] != None:
        del cursos[curso_id -1]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
