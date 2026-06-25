"""
Prompt templates.
"""

from rag.constants import DEFAULT_SYSTEM_PROMPT


def build_prompt(
    question: str,
    context: str,
) -> str:
    """
    Build a RAG prompt.
    """

    return f"""
{DEFAULT_SYSTEM_PROMPT}

Context:

{context}

Question:

{question}

Answer:
"""
