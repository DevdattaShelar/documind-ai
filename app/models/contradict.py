from pydantic import BaseModel


class ContradictRequest(BaseModel):
    document_1: str
    document_2: str
    topic: str


class ContradictResponse(BaseModel):
    conflict: bool
    reason: str