from pydantic import BaseModel


class CourseToSaveSchema(BaseModel):
    theme: str
    desires: str | None = None
    course: dict
