from pydantic import BaseModel, Field


class CourseToDeleteSchema(BaseModel):
    id: int = Field(gt=0)
