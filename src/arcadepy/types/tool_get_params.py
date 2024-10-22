# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolGetParams"]


class ToolGetParams(TypedDict, total=False):
    tool_id: Required[Annotated[str, PropertyInfo(alias="toolId")]]
    """Tool ID"""
