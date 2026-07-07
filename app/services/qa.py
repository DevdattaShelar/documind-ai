from app.core.config import settings
from app.models.qa import Citation, QAResponse
from app.services.llm import LLMService
from app.services.prompt_builder import PromptBuilder
from app.services.retriever import Retriever
from app.services.translator import TranslatorService


class QAService:

    def __init__(self):

        self.retriever = Retriever()
        self.llm = LLMService()
        self.translator = TranslatorService()

    def ask(
        self,
        question: str,
    ) -> QAResponse:

        language = self.translator.detect_language(question)

        print("Detected language:", language)

        translated_question = question

        if language.lower() != "english":
            translated_question = self.translator.translate_to_english(
            question
        )

        print("Translated question:", translated_question) 
        results = self.retriever.retrieve(translated_question)

        print("Results:", len(results))

        if results:
            print("Top score:", results[0].score)

        if not results:
            return QAResponse(
                answer="The provided documents do not contain enough information to answer this question.",
                citations=[],
            )

##        if results[0].score > settings.SIMILARITY_THRESHOLD:
            return QAResponse(
                answer="The provided documents do not contain enough information to answer this question.",
                citations=[],
            )

        prompt = PromptBuilder.build(
            translated_question,
            results,
        )

        answer = self.llm.generate(prompt)

        if language.lower() != "english":
            answer = self.translator.translate_from_english(
                answer,
                language,
            )

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