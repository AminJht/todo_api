# To-Do List RESTful API

A RESTful API for managing tasks, built with FastAPI and SQLite.

## Features
- Create, read, update, and delete tasks (CRUD operations).
- Mark tasks as completed or not.
- Interactive API documentation with Swagger UI.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/AminJht/todo-api.git
   cd todo-api
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pydantic
   ```
3. Initialize the database:
   ```bash
   python init.py
   ```
4. Run the API:
   ```bash
   uvicorn main:app --reload
   ```
5. Visit `http://localhost:8000/docs` for API documentation.

## Example Requests
- Create a task:
   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"title":"Buy milk","description":"From supermarket","completed":false}' http://localhost:8000/tasks
   ```
- Get all tasks:
   ```bash
   curl http://localhost:8000/tasks
   ```

## Technologies
- Python
- FastAPI
- SQLite
- Git

# todo_api
