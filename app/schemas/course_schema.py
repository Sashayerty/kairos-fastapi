from pydantic import BaseModel


class CourseSchema(BaseModel):
    theme: str
    desires: str | None = None
