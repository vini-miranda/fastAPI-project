from fastapi import FastAPI

app = FastAPI()

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
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int):
    curso = cursos[curso_id]
    curso.update({"id": curso_id})
    return curso


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", reload=True) 