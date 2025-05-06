from pydantic import BaseModel, Field


class ResponseSchema(BaseModel):
    detail: str = Field(
        description="detail of response",
        examples=[
            "bad request",
            "data stashed successfully",
        ],
    )
