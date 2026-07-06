from pathlib import Path
from typing import List
import uuid
from app.core.constants import (
    DOCUMENT_ID,
    SOURCE,
    PAGE,
    FILE_TYPE,
    PDF,
    TXT,
    MARKDOWN,
)
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    PyMuPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
)

from app.core.logging import logger


class DocumentLoader:
    """
    Service responsible for loading supported documents from disk.
    """

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".txt",
        ".md",
    }

    def load_document(self, path: Path) -> List[Document]:
        """
        Load a single document and enrich its metadata.

        Args:
            path: Path to the document.

        Returns:
            List of LangChain Document objects.
        """

        if not path.exists():
            raise FileNotFoundError(f"{path} does not exist.")

        suffix = path.suffix.lower()

        if suffix not in self.SUPPORTED_EXTENSIONS:
            raise ValueError(f"Unsupported file type: {suffix}")

        logger.info("Loading %s", path.name)

        if suffix == ".pdf":
            loader = PyMuPDFLoader(str(path))

        elif suffix == ".txt":
            loader = TextLoader(
                str(path),
                encoding="utf-8",
            )

        else:
            loader = UnstructuredMarkdownLoader(str(path))

        documents = loader.load()

        # One UUID per original document
        document_id = str(uuid.uuid4())

        for document in documents:
            document.metadata[DOCUMENT_ID] = document_id
            document.metadata[SOURCE] = path.name
            document.metadata[FILE_TYPE] = suffix.replace(".", "")
            document.metadata.setdefault(PAGE, 1)

        logger.info(
            "Loaded %d page(s) from %s",
            len(documents),
            path.name,
        )

        return documents

    def load_directory(self, directory: Path) -> List[Document]:
        """
        Load every supported document from a directory.

        Args:
            directory: Directory containing documents.

        Returns:
            List of LangChain Document objects.
        """

        if not directory.exists():
            raise FileNotFoundError(f"{directory} does not exist.")

        documents: List[Document] = []

        for file_path in sorted(directory.iterdir()):

            if not file_path.is_file():
                continue

            if file_path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                logger.warning(
                    "Skipping unsupported file: %s",
                    file_path.name,
                )
                continue

            try:
                documents.extend(
                    self.load_document(file_path)
                )

            except Exception as e:
                logger.exception(
                    "Failed to load %s: %s",
                    file_path.name,
                    e,
                )

        logger.info(
            "Loaded %d document page(s) in total",
            len(documents),
        )

        return documents