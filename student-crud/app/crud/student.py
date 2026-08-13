from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.course import Course
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate


async def create_student(
    db: AsyncSession,
    student_data: StudentCreate,
) -> Student:
    student = Student(
        name=student_data.name,
        email=student_data.email,
        phone=student_data.phone,
    )

    if student_data.course_ids:
        result = await db.execute(
            select(Course).where(
                Course.id.in_(student_data.course_ids)
            )
        )
        courses = list(result.scalars().all())

        if len(courses) != len(set(student_data.course_ids)):
            raise ValueError("One or more course IDs do not exist")

        student.enrolled_courses = courses

    db.add(student)
    await db.commit()
    await db.refresh(student)

    return student


async def get_students(
    db: AsyncSession,
) -> list[Student]:
    result = await db.execute(
        select(Student).options(
            selectinload(Student.enrolled_courses)
        )
    )
    return list(result.scalars().all())


async def get_student(
    db: AsyncSession,
    student_id: int,
) -> Student | None:
    result = await db.execute(
        select(Student)
        .options(selectinload(Student.enrolled_courses))
        .where(Student.id == student_id)
    )
    return result.scalar_one_or_none()


async def update_student(
    db: AsyncSession,
    student: Student,
    student_data: StudentUpdate,
) -> Student:
    if student_data.name is not None:
        student.name = student_data.name

    if student_data.email is not None:
        student.email = student_data.email

    if student_data.phone is not None:
        student.phone = student_data.phone

    if student_data.course_ids is not None:
        if len(student_data.course_ids) == 0:
            student.enrolled_courses = []
        else:
            result = await db.execute(
                select(Course).where(
                    Course.id.in_(student_data.course_ids)
                )
            )
            courses = list(result.scalars().all())

            if len(courses) != len(set(student_data.course_ids)):
                raise ValueError("One or more course IDs do not exist")

            student.enrolled_courses = courses

    await db.commit()
    await db.refresh(student)

    return student


async def delete_student(
    db: AsyncSession,
    student: Student,
) -> None:
    await db.delete(student)
    await db.commit()