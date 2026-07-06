from pathlib import Path

from langchain_community.document_loaders import (
    PyMuPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader
)


class DocumentLoader:

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".txt",
        ".md"
    }

    def load_document(self, path: Path):

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            loader = PyMuPDFLoader(str(path))

        elif suffix == ".txt":
            loader = TextLoader(str(path), encoding="utf-8")

        elif suffix == ".md":
            loader = UnstructuredMarkdownLoader(str(path))

        else:
            raise ValueError(f"Unsupported file type: {suffix}")

        documents = loader.load()

        return documents