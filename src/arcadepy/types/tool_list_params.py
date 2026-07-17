# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    filter: str
    """JSON metadata filter.

    Array fields (service_domains, operations): shorthand array or object with
    any_of/all_of/none_of operators (case-insensitive). Boolean fields: read_only,
    destructive, idempotent, open_world. Extras: case-sensitive key-value subset
    match.
    """

    include_all_versions: bool
    """Include all versions of each tool"""

    include_format: List[Literal["arcade", "openai", "anthropic", "mcp"]]
    """Comma separated tool formats that will be included in the response."""

    limit: int
    """Number of items to return (default: 25, max: 100)"""

    offset: int
    """Offset from the start of the list (default: 0)"""

    search: str
    """
    Case-insensitive literal substring matched against each tool's name, MCP server
    name, qualified name, and description; multiple whitespace-separated terms must
    all match. Max 2000 characters.
    """

    toolkit: str
    """Toolkit name"""

    user_id: str
    """User ID"""
