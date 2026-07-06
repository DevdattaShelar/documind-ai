from pathlib import Path

from app.core.logging import logger
from app.services.loader import DocumentLoader
from app.services.chunker import ChunkingService
from app.services.vectorstore import VectorStoreService


class IngestionService:

    def __init__(self):

        self.loader = DocumentLoader()

        self.chunker = ChunkingService()

        self.vector_store = VectorStoreService()

    def ingest_directory(
        self,
        directory: Path,
    ):

        logger.info("Starting ingestion...")

        documents = self.loader.load_directory(directory)

        chunks = self.chunker.chunk_documents(documents)

        self.vector_store.index_documents(chunks)

        logger.info(
            "Collection size: %d",
            self.vector_store.count(),
        )