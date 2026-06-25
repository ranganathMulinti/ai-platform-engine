"""
LLM provider interface.
"""

from abc import ABC, abstractmethod


class LLMProvider(ABC):
    """
    Base Large Language Model provider.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate text from a prompt.
        """
