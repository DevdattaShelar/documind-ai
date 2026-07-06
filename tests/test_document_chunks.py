from app.services.vectorstore import VectorStoreService

vector_store = VectorStoreService()

chunks = vector_store.get_chunks_by_source(
    "fastapi.md",
)

print(f"Chunks: {len(chunks)}")

print()

print(chunks[0].metadata)

print()

print(chunks[0].page_content[:500])