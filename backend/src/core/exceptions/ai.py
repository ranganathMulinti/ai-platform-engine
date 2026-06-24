from .base import PlatformError


class AIProviderError(PlatformError):
    """Base class for AI provider-related exceptions."""


class EmbeddingError(AIProviderError):
    """Exception raised when embedding generation fails."""


class LLMGenerationError(AIProviderError):
    """Exception raised when LLM generation fails."""
