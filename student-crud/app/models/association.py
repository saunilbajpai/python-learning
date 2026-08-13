from sqlalchemy import ForeignKey, Table, Column

from app.database import Base


student_courses = Table(
    "student_courses",
    Base.metadata,
    Column(
        "student_id",
        ForeignKey("students.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "course_id",
        ForeignKey("courses.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)