from pydantic import BaseModel, Field


class CourseSave(BaseModel):
    theme: str = Field(description="Theme of course", examples=["Python"])
    desires: str | None = Field(
        description="Desires of user", examples=["Basics of web developing"]
    )
    description_of_user: str | None = Field(
        default=None,
        description="Description of user",
        examples=["Noob in programming"],
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
