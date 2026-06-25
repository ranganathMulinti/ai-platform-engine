"""
Prompt registry.
"""

from prompts.constants import (
    DEFAULT_PROMPT_VERSION,
)

PROMPTS: dict[str, str] = {
    "rag": """
You are a helpful assistant.

Use only the supplied context.

Context:

{context}

Question:

{question}

Answer:
""",
    "summarization": """
Summarize the following document.

{text}
""",
    "extraction": """
Extract structured information from:

{text}
""",
}


def get_prompt(
    name: str,
) -> str:
    """
    Retrieve a prompt template.
    """

    if name not in PROMPTS:
        raise ValueError(f"Unknown prompt '{name}'.")

    return PROMPTS[name]


def prompt_version() -> str:
    """
    Current prompt version.
    """

    return DEFAULT_PROMPT_VERSION
