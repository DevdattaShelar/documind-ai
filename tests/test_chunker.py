from pathlib import Path

from app.services.loader import DocumentLoader
from app.services.chunker import ChunkingService

loader = DocumentLoader()
chunker = ChunkingService()

documents = loader.load_directory(Path("data"))

chunks = chunker.chunk_documents(documents)

print(f"Documents : {len(documents)}")
print(f"Chunks    : {len(chunks)}")
print()

for chunk in chunks[:3]:

    print(chunk.metadata)
    print(chunk.page_content[:120])
    print("-" * 80)