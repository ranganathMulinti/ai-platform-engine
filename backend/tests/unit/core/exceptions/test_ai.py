from core.exceptions import AIProviderError, EmbeddingError, LLMGenerationError, PlatformError


def test_ai_provider_error_inheritance():
    """Test that AIProviderError is a subclass of PlatformError."""
    assert issubclass(AIProviderError, PlatformError)


def test_embedding_error_message():
    """Test that EmbeddingError stores the message."""
    error = EmbeddingError("Embedding generation failed")
    assert error.message == "Embedding generation failed"


def test_llm_generation_error_message():
    """Test that LLMGenerationError stores the message."""
    error = LLMGenerationError("LLM generation failed")
    assert error.message == "LLM generation failed"


def test_string_representation():
    """Test that exceptions return the message when converted to string."""
    error = EmbeddingError("Embedding generation failed")
    assert str(error) == "Embedding generation failed"
