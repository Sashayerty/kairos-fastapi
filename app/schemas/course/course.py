from pydantic import BaseModel, Field


class Course(BaseModel):
    id: int = Field(gt=0)
    theme: str = Field(description="Theme of course", examples=["Python"])
    desires: str | None = Field(
        description="Desires of user", examples=["Basics of web developing"]
    )
    course: dict[str, dict[str, str]] = Field(
        description="Course dict",
        examples=[
            {
                "1": {"title": "Python Basics", "data": "..."},
                "2": {"title": "Python and Web", "data": "..."},
            }
        ],
    )
