from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.course import Course
from app.schemas.course import CourseCreate


async def create_course(
    db: AsyncSession,
    course_data: CourseCreate,
) -> Course:
    course = Course(
        name=course_data.name,
    )

    db.add(course)
    await db.commit()
    await db.refresh(course)

    return course


async def get_courses(
    db: AsyncSession,
) -> list[Course]:
    result = await db.execute(
        select(Course)
    )

    return list(result.scalars().all())


async def get_course(
    db: AsyncSession,
    course_id: int,
) -> Course | None:
    result = await db.execute(
        select(Course).where(
            Course.id == course_id
        )
    )

    return result.scalar_one_or_none()


async def delete_course(
    db: AsyncSession,
    course: Course,
) -> None:
    await db.delete(course)
    await db.commit()
