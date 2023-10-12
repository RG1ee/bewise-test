import datetime
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Question(Base):
    __tablename__ = "question"

    id: Mapped[int] = mapped_column(primary_key=True)
    question_id: Mapped[int]
    question: Mapped[str]
    answer: Mapped[str]
    created_at: Mapped[datetime.datetime]
