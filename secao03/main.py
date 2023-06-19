from fastapi import FastAPI
from routes import curso_router
from routes import calculadora_router

app = FastAPI(
    
    title="Projeto Fast API",
    version="0.0.1",
    description="API para estudos do framework FastAPI"
)
app.include_router(curso_router.api_router, tags=['cursos'])
app.include_router(calculadora_router.api_router, tags=['calculadora'])


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", debug=True, reload=True) 