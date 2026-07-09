from fastapi import FastAPI

app = FastAPI()

@app.post("/create-user")
def create_user(name:str, age:int):
    return{
        "name" : name,
        "age" : age
    }


from fastapi import FastAPI
from pydMain import BaseModel

app = FastAPI

class User(BaseModel):
    name : str
    age : int


@app.post("/create-user")
def create_user(users:User):
    return{
        "message" : "user created",
        "data": users
    }