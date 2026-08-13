from fastapi import FastAPI

from app.routers.student import router as student_router
from app.routers.course import router as course_router


app = FastAPI(
    title="Student CRUD API",
    version="1.0.0",
)


app.include_router(student_router)
app.include_router(course_router)


@app.get("/")
async def root():
    return {
        "message": "Student CRUD API is running"
    }