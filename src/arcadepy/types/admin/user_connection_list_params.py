# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UserConnectionListParams", "Provider", "User"]


class UserConnectionListParams(TypedDict, total=False):
    limit: int
    """Page size"""

    offset: int
    """Page offset"""

    provider: Provider

    user: User


class Provider(TypedDict, total=False):
    id: str
    """Provider ID"""


class User(TypedDict, total=False):
    id: str
    """User ID"""
