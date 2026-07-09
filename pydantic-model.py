from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# # creating schemas ----------------------
# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/create_user")
# def create_user(users:User):
#     return{
#         "Message" : "User created",
#         "Data" : users
#     }


# # creating nested model ----------------------------

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/user_created")
def user_created(users:User):
    return{
        "message":"user created!!",
        "data":users
    }
