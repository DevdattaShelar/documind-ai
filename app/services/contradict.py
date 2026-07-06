from app.services.llm import LLMService
from app.services.vectorstore import VectorStoreService


class ContradictService:
    """
    Compare two documents on a specific topic.
    """

    def __init__(self):

        self.vector_store = VectorStoreService()
        self.llm = LLMService()

    def compare(
        self,
        document_1: str,
        document_2: str,
        topic: str,
    ):

        doc1_chunks = self.vector_store.similarity_search_by_source(
            query=topic,
            source=document_1,
            k=3,
        )

        doc2_chunks = self.vector_store.similarity_search_by_source(
            query=topic,
            source=document_2,
            k=3,
        )

        context1 = "\n\n".join(
            chunk.page_content
            for chunk in doc1_chunks
        )

        context2 = "\n\n".join(
            chunk.page_content
            for chunk in doc2_chunks
        )

        prompt = f"""
You are comparing two documents.

Topic:
{topic}

-------------------------
Document 1 ({document_1})

{context1}

-------------------------
Document 2 ({document_2})

{context2}

-------------------------

Answer ONLY in this format:

Conflict: YES or NO

Reason:
<short explanation>

If neither document discusses the topic, answer:

Conflict: NO

Reason:
The documents do not provide enough information about the topic.
"""

        answer = self.llm.generate(prompt)

        conflict = answer.upper().startswith("CONFLICT: YES")

        return {
            "conflict": conflict,
            "reason": answer,
        }