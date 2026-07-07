from app.services.llm import LLMService


class TranslatorService:
    """
    Handles language detection and translation.
    """

    def __init__(self):
        self.llm = LLMService()

    def detect_language(self, text: str) -> str:

        prompt = f"""
Identify the language of this text.

Reply with ONLY one word.

Examples:
English
Hindi
Marathi
French
German

Text:
{text}
"""

        return self.llm.generate(prompt).strip()

    def translate_to_english(
        self,
        text: str,
    ) -> str:

        prompt = f"""
Translate the following text into English.

Input:
{text}

Output:
"""

        return self.llm.generate(
        prompt=prompt,
        system_prompt="""
You are a translation engine.

Your ONLY job is to translate.

Never answer the question.
Never explain.
Never summarize.

Return ONLY the translated text.
""",
    ).strip()

    def translate_from_english(
    self,
    text: str,
    language: str,
) -> str:

        return self.llm.generate(
        prompt=text,
        system_prompt=f"""
You are a professional translator.

Translate every input into {language}.

Rules:
- Return ONLY the translated text.
- Do NOT explain.
- Do NOT add quotes.
- Do NOT add labels.
""",
    ).strip()