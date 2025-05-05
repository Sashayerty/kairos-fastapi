from sqlalchemy import JSON, Column, Integer, String, Text

from app.models.db_session import SqlAlchemyBase
from app.schemas import Course


class CoursesModel(SqlAlchemyBase):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    theme = Column(String(255), nullable=False)
    desires_of_user = Column(Text, nullable=True)
    course = Column(JSON, nullable=False)

    @classmethod
    def from_pydantic(cls, course: Course) -> "CoursesModel":
        """Создает экземпляр модели БД из Pydantic-модели"""
        return cls(
            theme=course.theme,
            desires_of_user=course.desires,
            course=course.course,
        )
