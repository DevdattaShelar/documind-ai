from app.services.retriever import Retriever

retriever = Retriever()

question = "FastAPI क्या है?"

results = retriever.retrieve(
    question,
    k=3,
)

print(f"\nQuestion: {question}\n")

for i, result in enumerate(results, start=1):

    print("=" * 80)

    print(f"Result #{i}")

    print(f"Similarity Score : {result.score:.4f}")

    print(f"Source : {result.document.metadata['source']}")

    print()

    print(result.document.page_content[:300])