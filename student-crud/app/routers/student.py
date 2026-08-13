from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.student import (
    create_student,
    delete_student,
    get_student,
    get_students,
    update_student,
)
from app.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
)

router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_new_student(
    student_data: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    try:
        return await create_student(db, student_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[StudentResponse],
)
async def read_students(
    db: AsyncSession = Depends(get_db),
):
    return await get_students(db)


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
)
async def read_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    student = await get_student(db, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    return student


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
)
async def update_existing_student(
    student_id: int,
    student_data: StudentUpdate,
    db: AsyncSession = Depends(get_db),
):
    student = await get_student(db, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    try:
        return await update_student(db, student, student_data)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_existing_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    student = await get_student(db, student_id)
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    await delete_student(db, student)
