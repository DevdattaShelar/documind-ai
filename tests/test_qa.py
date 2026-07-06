from app.services.qa import QAService

qa = QAService()

question = "What is FastAPI?"

response = qa.ask(question)

print("=" * 80)
print("QUESTION")
print("=" * 80)
print(question)

print("\n" + "=" * 80)
print("ANSWER")
print("=" * 80)
print(response.answer)

print("\n" + "=" * 80)
print("CITATIONS")
print("=" * 80)

for citation in response.citations:
    print(f"Source   : {citation.source}")
    print(f"Page     : {citation.page}")
    print(f"Chunk ID : {citation.chunk_id}")
    print(f"Snippet  : {citation.snippet}")
    print("-" * 80)