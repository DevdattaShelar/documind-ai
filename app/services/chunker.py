from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    MarkdownHeaderTextSplitter,
)

from app.core.config import settings
from app.core.constants import (
    CHUNK_ID,
    FILE_TYPE,
    MARKDOWN,
)


class ChunkingService:

    def __init__(self):

        self.recursive_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            length_function=len,
        )

        self.markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
            ]
        )

    def _split_pdf_or_txt(
        self,
        document: Document,
    ) -> List[Document]:

        return self.recursive_splitter.split_documents([document])

    def _split_markdown(
        self,
        document: Document,
    ) -> List[Document]:

        header_docs = self.markdown_splitter.split_text(
            document.page_content
        )

        chunks = []

        for header_doc in header_docs:

            header_doc.metadata.update(document.metadata)

            split_chunks = self.recursive_splitter.split_documents(
                [header_doc]
            )

            chunks.extend(split_chunks)

        return chunks

    def chunk_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:

        chunked_documents = []

        chunk_counter = 0

        for document in documents:

            if document.metadata[FILE_TYPE] == MARKDOWN:

                chunks = self._split_markdown(document)

            else:

                chunks = self._split_pdf_or_txt(document)

            for chunk in chunks:

                chunk.metadata[CHUNK_ID] = chunk_counter

                chunk_counter += 1

            chunked_documents.extend(chunks)

        return chunked_documents