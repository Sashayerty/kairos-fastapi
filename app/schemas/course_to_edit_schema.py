from pydantic import BaseModel, Field


class CourseToEditSchema(BaseModel):
    id: int = Field(gt=0)
    desires: str
