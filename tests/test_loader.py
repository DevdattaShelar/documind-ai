from pathlib import Path

from app.loaders import DocumentLoader

loader = DocumentLoader()

docs = loader.load_document(Path("data/sample.txt"))

print(docs[0].page_content[:300])

print(docs[0].metadata)