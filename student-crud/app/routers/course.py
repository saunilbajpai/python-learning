from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.course import (
    create_course,
    delete_course,
    get_course,
    get_courses,
)
from app.database import get_db
from app.schemas.course import CourseCreate, CourseResponse

router = APIRouter(
    prefix="/courses",
    tags=["Courses"],
)


@router.post(
    "",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_course(
    course_data: CourseCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_course(
        db,
        course_data,
    )


@router.get(
    "",
    response_model=list[CourseResponse],
)
async def read_courses(
    db: AsyncSession = Depends(get_db),
):
    return await get_courses(db)


@router.get(
    "/{course_id}",
    response_model=CourseResponse,
)
async def read_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    course = await get_course(db, course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found",
        )
    return course


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_existing_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    course = await get_course(db, course_id)
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id {course_id} not found",
        )
    await delete_course(db, course)