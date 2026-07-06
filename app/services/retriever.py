from dataclasses import dataclass
from typing import List

from langchain_core.documents import Document

from app.services.vectorstore import VectorStoreService


@dataclass
class RetrievalResult:
    document: Document
    score: float


class Retriever:
    """
    Handles semantic retrieval from the vector database.
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

        retrieval_results = []

        for document, score in results:

            retrieval_results.append(
                RetrievalResult(
                    document=document,
                    score=score,
                )
            )

        return retrieval_results