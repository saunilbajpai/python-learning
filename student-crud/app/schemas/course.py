from pydantic import BaseModel, ConfigDict


class CourseCreate(BaseModel):
    name: str


class CourseResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)