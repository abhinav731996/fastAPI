from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id : int
    title : str
    completed : bool

# # to create todos -------------------------------
@app.post("/todos")
def create_todos(todo : Todo):
    todos.append(todo)
    return {
        "message" : "todo added",
        "data" : todo
    }

# # to get all todos ------------------------------
@app.get("/todos")
def get_todos():
    return todos

# # to get specific todos by using path params-----------------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return{ "error": "todo not found"}


# # to update specific todos -----------------------------
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] =updated_todo
            return{
                "message":"Data updated !!",
                "data":updated_todo
            }
    return{ "error": "todo not found"}


# # To delete specific todos ----------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return{"message":"Deleted !!"}
    return{ "error": "todo not found"}
    