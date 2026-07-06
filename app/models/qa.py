from pydantic import BaseModel


class Citation(BaseModel):
    source: str
    page: int
    chunk_id: int
    snippet: str


class QAResponse(BaseModel):
    answer: str
    citations: list[Citation]