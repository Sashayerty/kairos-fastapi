from pydantic import BaseModel

from app.schemas.course import Course


class CourseList(BaseModel):
    courses: list[Course] | str
    count_of_courses: int
