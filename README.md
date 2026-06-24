# Exception Framework for AI Platform Engine

## Purpose

This package provides a centralized exception handling system for the AI Platform Engine. It defines a hierarchy of exceptions to ensure consistent error handling across the platform.

## Exception Hierarchy

- `PlatformError`: Base class for all platform exceptions
- `APIError`: Base class for API-related exceptions
  - `ResourceNotFoundError`: Resource not found
  - `UnauthorizedError`: Authentication required but not provided
  - `ForbiddenError`: User lacks permission
- `DatabaseError`: Base class for database-related exceptions
  - `DatabaseConnectionError`: Database connection failure
  - `TransactionError`: Database transaction failure
- `ValidationError`: Validation failure
- `AIProviderError`: Base class for AI provider exceptions
  - `EmbeddingError`: Embedding generation failure
  - `LLMGenerationError`: LLM generation failure

## Usage Examples

