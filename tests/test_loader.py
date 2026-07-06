from pathlib import Path

from app.services.loader import DocumentLoader

loader = DocumentLoader()

documents = loader.load_directory(Path("data"))

print(f"Loaded {len(documents)} document(s)\n")

for document in documents:
    print(document.metadata)