from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List
from database import get_db
app = FastAPI()

class TaskCreate(BaseModel):
    title:str
    description:str | None = None
    completed:bool = False

class Task(TaskCreate):
    id:int

@app.get("/tasks" , response_model=List[Task])
def get_tasks():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, description, completed FROM tasks")
    tasks = [{"id":row["id"],"title":row["title"],"description":row["description"],"completed":row["completed"]} for row in cursor.fetchall()]
    conn.close()
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    conn = get_db()
    cursor=conn.cursor()
    cursor.execute("SELECT id ,title ,description ,completed FROM tasks WHERE id=?",(task_id,))
    task = cursor.fetchone()
    if task is None:
        raise HTTPException(status_code=404 ,detail="Task not found")
    return {"id":task["id"], "title":task["title"], "description" :task["description"], "completed":task["completed"]}

@app.post("/tasks", response_model=Task)
def create_task(task : TaskCreate):
    conn = get_db()
    cursor=conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, completed) VALUES (?,?,?)",
        (task.title, task.description, task.completed)
    )
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": task_id, "title": task.title, "description": task.description, "completed": task.completed }

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id : int , task : TaskCreate):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET title = ?, description = ?, completed = ? WHERE id = ?",
        (task.title, task.description, task.completed , task_id)
    )
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404 , detail="Task not found")
    conn.commit()
    conn.close()
    return {"id":task_id , "title":task.title, "description":task.description, "completed": task.completed}

@app.delete("/tasks/{task_id}")
def delete_task(task_id : int ):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404 , detail = "Task not found")
    conn.commit()
    conn.close()
    return {"massage":"task deleted"}
