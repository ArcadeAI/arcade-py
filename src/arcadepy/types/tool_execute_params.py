# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolExecuteParams"]


class ToolExecuteParams(TypedDict, total=False):
    tool_name: Required[str]

    inputs: object
    """JSON input to the tool, if any"""

    tool_version: str
    """Optional: if not provided, any version is used"""

    user_id: str
