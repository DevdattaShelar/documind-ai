from app.services.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What is FastAPI?",
    k=3,
)

print("\nRetrieved Documents\n")

for result in results:

    print("=" * 80)

    print(f"Score : {result.score:.4f}")

    print(f"Source: {result.document.metadata['source']}")

    print()

    print(result.document.page_content[:300])