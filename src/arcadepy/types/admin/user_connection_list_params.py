# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserConnectionListParams"]


class UserConnectionListParams(TypedDict, total=False):
    limit: int
    """Page size"""

    offset: int
    """Page offset"""

    provider_id: str
    """Provider ID"""

    user_id: str
    """User ID"""
