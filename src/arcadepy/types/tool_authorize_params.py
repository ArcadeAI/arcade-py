# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolAuthorizeParams"]


class ToolAuthorizeParams(TypedDict, total=False):
    tool_name: Required[str]

    user_id: Required[str]

    tool_version: str
    """Optional: if not provided, any version is used"""
