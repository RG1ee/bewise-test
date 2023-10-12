from datetime import datetime

from fastapi import HTTPException, status
import httpx

from src.config.settings import settings
from src.questions.services import QuestionService


async def get_question_request(questions_num: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.API_URL}{questions_num}")

        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error when requesting questions from an external API",
            )

    return response.json()


async def save_question_return_last(questions_num: int):
    remaining_questions = questions_num

    while remaining_questions > 0:
        questions = await get_question_request(remaining_questions)
        new_questions = [
            question
            for question in questions
            if not await QuestionService.get_one_or_none(id=question["id"])
        ]

        if new_questions:
            for new_question in new_questions:
                await QuestionService.insert_data(
                    question_id=new_question["id"],
                    question=new_question["question"],
                    answer=new_question["answer"],
                    created_at=datetime.strptime(
                        new_question["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
                    ),
                )
            remaining_questions -= len(new_questions)

    return await QuestionService.get_last_question()
