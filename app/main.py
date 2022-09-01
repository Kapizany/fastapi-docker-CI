from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/{id}")
async def hello(id:str):
    return {"message": f"Hello {id}"}

@app.get("/bye/{name}")
async def bye(name:str):
    return {"message": f"Bye {name}"}

@app.get("/sum/{number1}/{number2}")
async def sum(number1:int, number2: int):
    return {"message": f"The sum is {number1 + number2}"}

@app.get("/sub/{number1}/{number2}")
async def sub(number1:int, number2: int):
    return {"message": f"The sub is {number1 - number2}"}

@app.get("/mult/{number1}/{number2}")
async def mult(number1:int, number2: int):
    return {"message": f"The mult is {number1*number2}"}