from sqlalchemy.orm import relationship
from app.models.association import student_courses
from typing import TYPE_CHECKING
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
if TYPE_CHECKING:
    from app.models.student import Student

class course(Base):
    __tablename__ = "courses"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False)
    students: Mapped[list["Student"]] = relationship(
        secondary=student_courses,
        back_populates="enrolled_courses",
    )

