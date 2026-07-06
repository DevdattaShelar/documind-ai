from dataclasses import dataclass
from typing import List

from langchain_core.documents import Document

from app.core.constants import (
    CHUNK_ID,
    PAGE,
    SOURCE,
    DOCUMENT_ID,
)

from app.services.vectorstore import VectorStoreService


@dataclass
class RetrievalResult:
    document: Document
    score: float

    @property
    def source(self) -> str:
        return self.document.metadata[SOURCE]

    @property
    def page(self) -> int:
        return self.document.metadata[PAGE]

    @property
    def chunk_id(self) -> int:
        return self.document.metadata[CHUNK_ID]

    @property
    def document_id(self) -> str:
        return self.document.metadata[DOCUMENT_ID]

    @property
    def snippet(self) -> str:
        return self.document.page_content[:200]


class Retriever:
    """
    Retrieves the most relevant documents from the vector store.
    """

    def __init__(self):
        self.vector_store = VectorStoreService()

    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> List[RetrievalResult]:

        results = self.vector_store.similarity_search_with_score(
            query=query,
            k=k,
        )

        retrieval_results: List[RetrievalResult] = []
        seen = set()

        for document, score in results:

            key = (
                document.metadata[DOCUMENT_ID],
                document.metadata[CHUNK_ID],
            )

            if key in seen:
                continue

            seen.add(key)

            retrieval_results.append(
                RetrievalResult(
                    document=document,
                    score=score,
                )
            )

        return retrieval_results