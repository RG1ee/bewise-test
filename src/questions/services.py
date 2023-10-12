from sqlalchemy import select
from src.database import Question
from src.base.services import BaseService
from src.database.db import async_session


class QuestionService(BaseService):
    model = Question

    @classmethod
    async def get_last_question(cls):
        async with async_session() as session:
            query = select(cls.model.__table__.columns).order_by(cls.model.id.desc())
            result = await session.execute(query)
            return result.mappings().first()
