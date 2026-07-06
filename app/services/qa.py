from app.models.qa import Citation, QAResponse
from app.services.llm import LLMService
from app.services.prompt_builder import PromptBuilder
from app.services.retriever import Retriever


class QAService:

    def __init__(self):

        self.retriever = Retriever()
        self.llm = LLMService()

    def ask(self, question: str) -> QAResponse:

        results = self.retriever.retrieve(question)

        prompt = PromptBuilder.build(question, results)

        answer = self.llm.generate(prompt)

        citations = []

        for result in results:

            citations.append(
                Citation(
                    source=result.source,
                    page=result.page,
                    chunk_id=result.chunk_id,
                    snippet=result.snippet,
                )
            )

        return QAResponse(
            answer=answer,
            citations=citations,
        )