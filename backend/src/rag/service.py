"""
RAG service.
"""

from llm.base import LLMProvider
from rag.prompts import build_prompt
from rag.schemas import (
    RAGRequest,
    RAGResponse,
)
from retrieval.base import Retriever


class RAGService:
    """
    Retrieval-Augmented Generation service.
    """

    def __init__(
        self,
        retriever: Retriever,
        llm: LLMProvider,
    ) -> None:
        self.retriever = retriever
        self.llm = llm

    def ask(
        self,
        request: RAGRequest,
    ) -> RAGResponse:
        """
        Execute a RAG request.
        """

        retrieved = self.retriever.retrieve(
            request.question,
            request.top_k,
        )

        context = [chunk.text for chunk in retrieved.chunks]

        prompt = build_prompt(
            question=request.question,
            context="\n\n".join(context),
        )

        answer = self.llm.generate(
            prompt,
        )

        return RAGResponse(
            answer=answer,
            context=context,
        )
