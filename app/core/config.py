from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()


@dataclass(frozen=True)
class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

    # LLM
    LLM_MODEL: str = os.getenv(
        "LLM_MODEL",
        "llama-3.1-8b-instant",
    )

    # Embeddings
    EMBEDDING_MODEL: str = os.getenv(
        "EMBEDDING_MODEL",
        "BAAI/bge-small-en-v1.5",
    )

    # Vector DB
    CHROMA_PATH: str = "chroma_db"

    # Chunking
    CHUNK_SIZE: int = 800
    CHUNK_OVERLAP: int = 150

    # Retrieval
    TOP_K: int = 5
    SIMILARITY_THRESHOLD: float = 0.45


settings = Settings()