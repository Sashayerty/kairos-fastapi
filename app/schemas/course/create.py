from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    theme: str = Field(description="Theme of course", examples=["Python"])
    desires: str | None = Field(
        description="Desires of user", examples=["Basics of web developing"]
    )
