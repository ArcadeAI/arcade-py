# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatResponse", "Choice", "ChoiceMessage", "ChoiceMessageToolCall", "ChoiceMessageToolCallFunction", "Usage"]


class ChoiceMessageToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ChoiceMessageToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ChoiceMessageToolCallFunction] = None

    type: Optional[Literal["function"]] = None


class ChoiceMessage(BaseModel):
    content: str
    """The content of the message."""

    role: str
    """The role of the author of this message.

    One of system, user, tool, or assistant.
    """

    name: Optional[str] = None
    """tool Name"""

    tool_call_id: Optional[str] = None
    """tool_call_id"""

    tool_calls: Optional[List[ChoiceMessageToolCall]] = None
    """tool calls if any"""


class Choice(BaseModel):
    finish_reason: Optional[str] = None

    index: Optional[int] = None

    logprobs: Optional[object] = None

    message: Optional[ChoiceMessage] = None


class Usage(BaseModel):
    completion_tokens: Optional[int] = None

    prompt_tokens: Optional[int] = None

    total_tokens: Optional[int] = None


class ChatResponse(BaseModel):
    id: Optional[str] = None

    choices: Optional[List[Choice]] = None

    created: Optional[int] = None

    model: Optional[str] = None

    object: Optional[str] = None

    system_fingerprint: Optional[str] = None

    usage: Optional[Usage] = None
