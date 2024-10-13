# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatMessageParam", "ToolCall", "ToolCallFunction"]


class ToolCallFunction(TypedDict, total=False):
    arguments: str

    name: str


class ToolCall(TypedDict, total=False):
    id: str

    function: ToolCallFunction

    type: Literal["function"]


class ChatMessageParam(TypedDict, total=False):
    content: Required[str]
    """The content of the message."""

    role: Required[str]
    """The role of the author of this message.

    One of system, user, tool, or assistant.
    """

    name: str
    """tool Name"""

    tool_call_id: str
    """tool_call_id"""

    tool_calls: Iterable[ToolCall]
    """tool calls if any"""
