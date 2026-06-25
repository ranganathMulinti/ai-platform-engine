"""
Gemini provider.
"""

from core.dependencies import get_settings
from google import genai
from llm.base import LLMProvider
from llm.constants import DEFAULT_MODEL

settings = get_settings()


class GeminiProvider(LLMProvider):
    """
    Gemini implementation.
    """

    def __init__(self) -> None:
        self.client = genai.Client(
            api_key=settings.gemini_api_key,
        )

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate text.
        """

        response = self.client.models.generate_content(
            model=DEFAULT_MODEL,
            contents=prompt,
        )

        if response.text is None:
            return ""

        return response.text
