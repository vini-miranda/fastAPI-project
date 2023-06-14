from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"msg" : "Projeto FastAPI"}

""" if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app") """