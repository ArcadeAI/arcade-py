# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ToolCountExecutionsParams"]


class ToolCountExecutionsParams(TypedDict, total=False):
    end_time: str
    """Only executions recorded at or before this RFC 3339 timestamp"""

    outcome: Literal["success", "failure"]
    """Filter by outcome"""

    start_time: str
    """Only executions recorded at or after this RFC 3339 timestamp"""

    tool_name: str
    """Filter by tool name (case-insensitive substring match)"""

    toolkit_name: str
    """Filter by exact toolkit name"""
