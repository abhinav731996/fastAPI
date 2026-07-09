from fastapi import FastAPI

app = FastAPI()

# Home route 
@app.get("/")
def home():
    return{"message": "Welcome to fastapi"}

# About route
@app.get("/about")
def about():
    return{"message": "Welcome to about page"}

# User page
@app.get("/users")
def users():
    return{
        "users" : ["Abhinav", "Sahil", "Dinesh"]
    }
