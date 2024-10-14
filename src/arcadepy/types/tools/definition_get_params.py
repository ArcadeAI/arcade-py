# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["DefinitionGetParams"]


class DefinitionGetParams(TypedDict, total=False):
    director_id: Required[Annotated[str, PropertyInfo(alias="directorId")]]
    """Director ID"""

    tool_id: Required[Annotated[str, PropertyInfo(alias="toolId")]]
    """Tool ID"""
