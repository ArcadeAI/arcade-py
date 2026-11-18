# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ToolListExecutionsParams"]


class ToolListExecutionsParams(TypedDict, total=False):
    end_time: str
    """Only executions recorded at or before this RFC 3339 timestamp"""

    failure_reason: str
    """Filter to runs with a failed attempt whose error message contains this text (case-insensitive)"""

    limit: int
    """Number of items to return (default: 100, max: 25000)"""

    offset: int
    """Offset from the start of the list (default: 0)"""

    outcome: Literal["success", "failure"]
    """Filter by outcome"""

    start_time: str
    """Only executions recorded at or after this RFC 3339 timestamp"""

    tool_name: str
    """Filter by tool name (case-insensitive substring match)"""

    toolkit_name: str
    """Filter by exact toolkit name"""

    user_id: str
    """Filter by the user the execution ran for"""
