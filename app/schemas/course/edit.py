from pydantic import BaseModel, Field


class CourseEdit(BaseModel):
    desires: str | None = Field(
        description="Desires of user",
        examples=["Add paragraph about web developing"],
    )
