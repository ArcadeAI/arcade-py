# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatMessage", "ToolCall", "ToolCallFunction"]


class ToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ToolCall(BaseModel):
    id: Optional[str] = None

    function: Optional[ToolCallFunction] = None

    type: Optional[Literal["function"]] = None


class ChatMessage(BaseModel):
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

    tool_calls: Optional[List[ToolCall]] = None
    """tool calls if any"""
