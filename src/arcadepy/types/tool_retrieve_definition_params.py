# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolRetrieveDefinitionParams"]


class ToolRetrieveDefinitionParams(TypedDict, total=False):
    director_id: Required[str]
    """Director ID"""

    tool_id: Required[str]
    """Tool ID"""
