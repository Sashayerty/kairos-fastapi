from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    theme: str = Field(description="Theme of course", examples=["Python"])
    desires_of_user: str | None = Field(
        default=None,
        description="Desires of user",
        examples=["Basics of web developing"],
    )
    description_of_user: str | None = Field(
        default=None,
        description="Description of user",
        examples=["Noob in programming"],
    )
