"""
Conversation service.
"""

from conversation.schemas import (
    ChatMessage,
    ChatRequest,
    ChatResponse,
)
from rag.schemas import (
    RAGRequest,
)
from rag.service import RAGService


class ConversationService:
    """
    Conversation orchestration.
    """

    def __init__(
        self,
        rag: RAGService,
    ) -> None:
        self.rag = rag

    def chat(
        self,
        request: ChatRequest,
    ) -> ChatResponse:
        """
        Execute one chat turn.
        """

        rag_response = self.rag.ask(
            RAGRequest(
                question=request.message,
            )
        )

        return ChatResponse(
            answer=rag_response.answer,
            messages=[
                ChatMessage(
                    role="user",
                    content=request.message,
                ),
                ChatMessage(
                    role="assistant",
                    content=rag_response.answer,
                ),
            ],
        )
