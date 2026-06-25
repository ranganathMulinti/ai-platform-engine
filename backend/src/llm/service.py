"""
LLM service.
"""

from llm.base import LLMProvider
from llm.schemas import (
    GenerationRequest,
    GenerationResponse,
)


class LLMService:
    """
    LLM application service.
    """

    def __init__(
        self,
        provider: LLMProvider,
    ) -> None:
        self.provider = provider

    def generate(
        self,
        request: GenerationRequest,
    ) -> GenerationResponse:
        """
        Generate text.
        """

        text = self.provider.generate(
            request.prompt,
        )

        return GenerationResponse(
            text=text,
        )
