from pathlib import Path

from app.services.loader import DocumentLoader
from app.services.chunker import ChunkingService
from app.services.vectorstore import VectorStoreService

loader = DocumentLoader()
chunker = ChunkingService()
vector_store = VectorStoreService()

# Optional: start with a clean database
vector_store.reset()

documents = loader.load_directory(Path("data"))

print(f"Loaded {len(documents)} document pages")

chunks = chunker.chunk_documents(documents)

print(f"Created {len(chunks)} chunks")

vector_store.index_documents(chunks)

print(f"Indexed {vector_store.count()} chunks")