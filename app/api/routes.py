from fastapi import APIRouter
from pydantic import BaseModel

from app.models.contradict import (
    ContradictRequest,
    ContradictResponse,
)

from app.services.contradict import ContradictService
from app.services.qa import QAService

router = APIRouter()

qa_service = QAService()
contradict_service = ContradictService()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: AskRequest):

    return qa_service.ask(
        request.question,
    )


@router.post(
    "/contradict",
    response_model=ContradictResponse,
)
def contradict(
    request: ContradictRequest,
):

    result = contradict_service.compare(
        document_1=request.document_1,
        document_2=request.document_2,
        topic=request.topic,
    )

    return ContradictResponse(
        conflict=result["conflict"],
        reason=result["reason"],
    )