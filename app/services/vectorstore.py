from typing import List

from langchain_core.documents import Document
from langchain_chroma import Chroma

from app.core.config import settings
from app.core.constants import SOURCE
from app.core.embeddings import embedding_model
from app.core.logging import logger


# Singleton Chroma instance
_vector_store = Chroma(
    collection_name="documents",
    persist_directory=settings.CHROMA_PATH,
    embedding_function=embedding_model,
)


class VectorStoreService:
    """
    Handles indexing and retrieval using ChromaDB.
    """

    def __init__(self):
        self.vector_store = _vector_store

    def index_documents(
        self,
        documents: List[Document],
    ) -> None:

        logger.info("Indexing %d chunks...", len(documents))

        self.vector_store.add_documents(documents)

        logger.info("Indexing completed.")

    def similarity_search(
        self,
        query: str,
        k: int = 5,
    ) -> List[Document]:

        return self.vector_store.similarity_search(
            query=query,
            k=k,
        )

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 5,
    ):

        return self.vector_store.similarity_search_with_score(
            query=query,
            k=k,
        )
    def similarity_search_by_source(
        self,
        query: str,
        source: str,
        k: int = 3,
    ) -> List[Document]:
        """
        Retrieve the most relevant chunks from a specific document.
        """

        return self.vector_store.similarity_search(
            query=query,
            k=k,
            filter={
                "source": source,
            },
        )
   
    def get_chunks_by_source(
        self,
        source: str,
    ) -> List[Document]:
        """
        Return every chunk belonging to a source document.
        """

        results = self.vector_store.get(
            where={
                SOURCE: source,
            },
            include=["documents", "metadatas"],
        )

        documents = []

        for text, metadata in zip(
            results["documents"],
            results["metadatas"],
        ):

            documents.append(
                Document(
                    page_content=text,
                    metadata=metadata,
                )
            )

        return documents

    def count(self) -> int:

        return self.vector_store._collection.count()

    def reset(self) -> None:

        logger.warning("Deleting Chroma collection...")

        self.vector_store.delete_collection()

        global _vector_store

        _vector_store = Chroma(
            collection_name="documents",
            persist_directory=settings.CHROMA_PATH,
            embedding_function=embedding_model,
        )

        self.vector_store = _vector_store

        logger.info("Collection recreated.")