from fastapi import FastAPI

app = FastAPI()

# optional parameter
@app.get("/users")
def get_user(name: str = None):
    return{
        "Name": name
    }

# default parameter
@app.get("/products")
def get_user(limit: int = 10):
    return{ "limit": limit}

# multipule querry params
@app.get("/items")
def get_user(name: str = None, price: int = 0):
    return{
        "name" : name,
        "price" : price
    }