# To-Do List RESTful API

A simple and fast RESTful API for managing a to-do list, built with **FastAPI** (Python) and **SQLite**.

## What It Does
- Create, read, update, and delete tasks via RESTful endpoints.
- Lightweight backend for web or mobile apps.

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/todo-api.git
   cd todo-api
   ```

2. **Install Dependencies**:
   Ensure Python 3.7+ is installed, then run:
   ```bash
   pip install fastapi uvicorn sqlalchemy
   ```

3. **Run the API**:
   ```bash
   uvicorn main:app --reload
   ```
   API runs at `http://localhost:8000`.

## Using the API
All endpoints are under `http://localhost:8000/api`. Use cURL or tools like Postman to interact.

### 1. Create a Task
- **Request**: `POST /api/tasks`
- **Body**:
  ```json
  {
    "title": "Buy bread",
    "description": "Get stone-baked bread by evening",
    "due_date": "2025-05-04"
  }
  ```
- **cURL**:
  ```bash
  curl -X POST http://localhost:8000/api/tasks -H "Content-Type: application/json" -d '{"title":"Buy bread","description":"Get stone-baked bread by evening","due_date":"2025-05-04"}'
  ```
- **Response**: Returns the created task with an ID.

### 2. List All Tasks
- **Request**: `GET /api/tasks`
- **cURL**:
  ```bash
  curl http://localhost:8000/api/tasks
  ```
- **Response**: Returns a JSON array of all tasks.

### 3. Update a Task
- **Request**: `PUT /api/tasks/{id}`
- **Body**:
  ```json
  {
    "title": "Buy stone-baked bread",
    "description": "Get two loaves"
  }
  ```
- **cURL** (replace `{id}` with task ID, e.g., `1`):
  ```bash
  curl -X PUT http://localhost:8000/api/tasks/1 -H "Content-Type: application/json" -d '{"title":"Buy stone-baked bread","description":"Get two loaves"}'
  ```
- **Response**: Returns the updated task.

### 4. Delete a Task
- **Request**: `DELETE /api/tasks/{id}`
- **cURL** (replace `{id}` with task ID, e.g., `1`):
  ```bash
  curl -X DELETE http://localhost:8000/api/tasks/1
  ```
- **Response**: No content (204 status).

## Testing
- Use the interactive **Swagger UI** at `http://localhost:8000/docs` for testing endpoints.
- Or use the cURL commands above.