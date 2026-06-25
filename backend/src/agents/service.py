"""
Agent implementation.
"""

from agents.base import Agent
from agents.schemas import (
    AgentRequest,
    AgentResponse,
)
from conversation.schemas import (
    ChatRequest,
)
from conversation.service import (
    ConversationService,
)


class AssistantAgent(Agent):
    """
    Default assistant agent.
    """

    def __init__(
        self,
        conversation: ConversationService,
    ) -> None:
        self.conversation = conversation

    def invoke(
        self,
        request: AgentRequest,
    ) -> AgentResponse:
        """
        Execute the assistant.
        """

        response = self.conversation.chat(
            ChatRequest(
                conversation_id="default",
                message=request.message,
            )
        )

        return AgentResponse(
            answer=response.answer,
        )
