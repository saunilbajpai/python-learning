from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.schemas.course import CourseResponse


class StudentCreate(BaseModel):
    name: str
    email: str
    phone: str | None = None
    course_ids: list[int] = []


class StudentUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    phone: str | None = None
    course_ids: list[int] | None = None


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str | None
    created_at: datetime
    enrolled_courses: list[CourseResponse]

    model_config = ConfigDict(from_attributes=True)