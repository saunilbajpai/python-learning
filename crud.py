from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

# Initialize FastAPI application instance
app = FastAPI()

# Pydantic model defining the schema and validation for a Student
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str
    email: EmailStr | None = None  # Optional email field with validation

# In-memory storage for students
students: list[Student] = []

# CREATE: Add a new student
@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return student

# READ: Retrieve all students
@app.get("/students")
def get_students():
    return students

# READ: Retrieve a single student by their ID
@app.get("/students/{student_id}")
def get_single_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    # Return 404 if student is not found
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# UPDATE: Modify an existing student by ID
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for i, existing_student in enumerate(students):
        if existing_student.id == student_id:
            students[i] = student
            return student
    # Return 404 if student to update does not exist
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

# DELETE: Remove a student by ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for i, student in enumerate(students):
        if student.id == student_id:
            students.pop(i)
            return {"message": "Student deleted"}
    # Return 404 if student to delete does not exist
    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )