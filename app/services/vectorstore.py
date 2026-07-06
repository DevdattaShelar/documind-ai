from typing import List

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.config import settings
from app.core.logging import logger


class VectorStoreService:
    """Handles indexing and retrieval using ChromaDB."""

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

        self.vector_store = Chroma(
            collection_name="documents",
            persist_directory=settings.CHROMA_PATH,
            embedding_function=self.embedding_model,
        )

    def index_documents(self, documents: List[Document]) -> None:
        logger.info("Indexing %d chunks...", len(documents))
        self.vector_store.add_documents(documents)
        logger.info("Indexing complete.")

    def similarity_search(self, query: str, k: int = 5):
        return self.vector_store.similarity_search(query, k=k)

    def similarity_search_with_score(self, query: str, k: int = 5):
        return self.vector_store.similarity_search_with_score(query, k=k)

    def count(self) -> int:
        return self.vector_store._collection.count()

    def reset(self) -> None:
        logger.warning("Resetting vector collection...")
        self.vector_store.delete_collection()

        self.vector_store = Chroma(
            collection_name="documents",
            persist_directory=settings.CHROMA_PATH,
            embedding_function=self.embedding_model,
        )