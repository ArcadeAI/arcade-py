# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FormattedGetParams"]


class FormattedGetParams(TypedDict, total=False):
    tool_id: Required[Annotated[str, PropertyInfo(alias="toolId")]]
    """Tool ID"""

    format: str
    """Provider format"""
