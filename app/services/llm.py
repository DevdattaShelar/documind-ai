from groq import Groq

from app.core.config import settings


class LLMService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY,
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            temperature=0,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        content = response.choices[0].message.content

        if content is None:
            raise RuntimeError("LLM returned an empty response.")

        return content