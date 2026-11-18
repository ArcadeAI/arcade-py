# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HookListParams"]


class HookListParams(TypedDict, total=False):
    hook_point: str
    """Filter by hook point"""

    limit: int
    """Limit"""

    offset: int
    """Offset"""

    plugin_id: str
    """Filter by plugin ID"""

    status: str
    """Filter by status"""
