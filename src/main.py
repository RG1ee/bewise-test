from fastapi import FastAPI

from src.questions.routers import router as question_router


app = FastAPI(title="BEWISE API")

app.include_router(question_router, prefix="/api")
