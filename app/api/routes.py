from pydantic import BaseModel

from fastapi import APIRouter

from app.services.qa import QAService

router = APIRouter()

qa_service = QAService()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: AskRequest):

    return qa_service.ask(request.question)