# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    include_all_versions: bool
    """Include all versions of each tool"""

    include_format: List[Literal["arcade", "openai", "anthropic"]]
    """Comma separated tool formats that will be included in the response."""

    limit: int
    """Number of items to return (default: 25, max: 100)"""

    offset: int
    """Offset from the start of the list (default: 0)"""

    toolkit: str
    """Toolkit name"""

    user_id: str
    """User ID"""
