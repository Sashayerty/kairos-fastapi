from sqlmodel import JSON, Column, Field, SQLModel

from app.schemas import Course


class Courses(SQLModel, table=True):
    id: int | None = Field(
        default=None,
        primary_key=True,
        description="id of course",
    )
    theme: str = Field(description="Theme of course")
    desires_of_user: str | None = Field(
        default=None,
        description="Desires of user",
    )
    description_of_user: str | None = Field(
        default=None,
        description="Description of user",
    )
    course: Course = Field(
        sa_column=Column(JSON),
        description="Course dict",
    )
