from fastapi import FastAPI
from src.utils.db import Base, engine
# from src.tasks.models import TaskModel
from src.tasks.router import task_routes


Base.metadata.create_all(engine)
#When our server runs, initially it will try to get connect with the database and 
# if success all the table created in the application will get stored in database 

app = FastAPI(title = "Welcome to the Task Management Application")
@app.get("/")
def home():
    return {"status":"Welcome to the Task Management Application"}

app.include_router(task_routes)