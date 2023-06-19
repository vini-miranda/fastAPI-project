from typing import Optional, Any
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Query
from fastapi import Response
from fastapi import Header
from fastapi import Depends
from models import Curso
from time import sleep

app = FastAPI()

def db_simulator():
    try:
        print("Abrindo conexão com banco de dados...")
        sleep(1)
    finally:
        print("fechando conexão com banco de dados...")
        sleep(1)


cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos",
        "aulas": 30,
        "horas": 14
    },
    3: {
        "titulo": "Lógica de Programação",
        "aulas": 42,
        "horas": 23
    }
}

@app.get('/cursos')
async def get_cursos(db: Any = Depends(db_simulator)):
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int, db: Any = Depends(db_simulator)):
    try:
        curso = cursos[curso_id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")    

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(db_simulator)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(db_simulator)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id: int, db: Any = Depends(db_simulator)):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.get('/calculadora')
async def calculo(
    a: int = Query(default=None, gt=5), 
    b: int = Query(default=None, lt=10), 
    c: Optional[int] = 0,
    x_geek: str = Header(default=None)
):
    soma = a + b + c
    print(f'X_GEEK: {x_geek}')
    return {"resultado" : soma}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", debug=True, reload=True) 