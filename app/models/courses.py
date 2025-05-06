from sqlmodel import JSON, Column, Field, SQLModel


class Courses(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    theme: str
    desires_of_user: str | None
    course: dict = Field(sa_column=Column(JSON))
