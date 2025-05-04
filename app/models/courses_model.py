from sqlalchemy import JSON, Column, Integer, String, Text

from app.models.db_session import SqlAlchemyBase


class CoursesModel(SqlAlchemyBase):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    theme = Column(String, nullable=False)
    desires_of_user = Column(Text, nullable=True)
    course = Column(JSON, nullable=False)
