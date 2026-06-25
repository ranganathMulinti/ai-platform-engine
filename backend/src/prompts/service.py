"""
Prompt service.
"""

from prompts.registry import (
    get_prompt,
)
from prompts.schemas import (
    PromptRenderRequest,
    PromptRenderResponse,
)


class PromptService:
    """
    Prompt rendering service.
    """

    def render(
        self,
        request: PromptRenderRequest,
    ) -> PromptRenderResponse:
        """
        Render a prompt.
        """

        template = get_prompt(
            request.name,
        )

        rendered = template.format(
            **request.variables,
        )

        return PromptRenderResponse(
            prompt=rendered,
        )
