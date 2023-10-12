from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class QuestionRequest(BaseModel):
    questions_num: int = Field(..., ge=1)


class QuestionResponse(BaseModel):
    question_id: int
    question: str
    answer: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
