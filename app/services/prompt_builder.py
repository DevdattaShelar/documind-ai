from typing import List

from app.services.retriever import RetrievalResult


class PromptBuilder:
    """
    Builds prompts for the LLM using retrieved context.
    """

    @staticmethod
    def build(
        question: str,
        results: List[RetrievalResult],
    ) -> str:

        context = ""

        for result in results:

            context += (
                f"Source: {result.source}\n"
                f"Page: {result.page}\n"
                f"Chunk: {result.chunk_id}\n\n"
                f"{result.document.page_content}\n\n"
                "-------------------------\n\n"
            )

        prompt = f"""
You are an AI assistant that answers questions ONLY using the provided context.

Rules:

1. Use ONLY the context below.
2. Do NOT use outside knowledge.
3. If the answer is not present in the context, reply exactly:
   "The provided documents do not contain enough information to answer this question."
4. Be concise and factual.
5. Do NOT mention or invent citations, sources, pages, or chunk numbers in your answer.

Context:

{context}

Question:
{question}

Answer:
"""

        return prompt.strip()