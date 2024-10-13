# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolExecuteParams"]


class ToolExecuteParams(TypedDict, total=False):
    inputs: Required[str]
    """Serialized JSON string"""

    tool_name: Required[str]

    tool_version: Required[str]

    user_id: Required[str]
