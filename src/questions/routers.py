from fastapi import APIRouter

from src.questions.schemas import QuestionRequest, QuestionResponse
from src.questions.utils import save_question_return_last


router = APIRouter(prefix="/questions", tags=["Question"])


@router.post(
    path="/get_questions",
    response_model=QuestionResponse,
)
async def get_question(payload: QuestionRequest):
    result = await save_question_return_last(payload.questions_num)
    return result
