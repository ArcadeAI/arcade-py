# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PluginListParams"]


class PluginListParams(TypedDict, total=False):
    binding_type: str
    """Binding type filter (e.g., 'tenant')"""

    limit: int
    """Limit"""

    offset: int
    """Offset"""
