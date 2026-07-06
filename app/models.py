from pydantic import BaseModel

class AskRequest(BaseModel):
    question: str


class Citation(BaseModel):
    source: str
    page: int
    chunk_id: int
    snippet: str


class AskResponse(BaseModel):
    answer: str
    confidence: float
    language: str
    citations: list[Citation]


class ContradictRequest(BaseModel):
    doc1: str
    doc2: str
    topic: str


class ContradictResponse(BaseModel):
    conflict: bool
    reasoning: str
    citations: list[Citation]