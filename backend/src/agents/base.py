"""
Base agent interface.
"""

from abc import ABC, abstractmethod

from agents.schemas import (
    AgentRequest,
    AgentResponse,
)


class Agent(ABC):
    """
    Base AI Agent.
    """

    @abstractmethod
    def invoke(
        self,
        request: AgentRequest,
    ) -> AgentResponse:
        """
        Execute the agent.
        """
