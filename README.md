# FastAPI Learning 🚀

A beginner-to-intermediate guide and code repository for learning **FastAPI** with Python.

## 📁 Repository Structure

- **`main.py`**: Introduction to FastAPI, setting up the application, basic root endpoint, and path & query parameters.
- **`crud.py`**: In-memory Student CRUD (Create, Read, Update, Delete) REST API with Pydantic model validation (`BaseModel`, `EmailStr`) and custom HTTP exceptions.

## 🛠️ How to Run

1. **Activate Virtual Environment**:
   ```bash
   .venv\Scripts\activate
   ```

2. **Run FastAPI Server with Auto-Reload**:
   ```bash
   fastapi dev crud.py
   # or
   fastapi dev main.py
   ```

3. **Interactive API Documentation**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
