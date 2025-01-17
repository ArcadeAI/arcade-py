# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthStatusParams"]


class AuthStatusParams(TypedDict, total=False):
    id: Required[str]
    """Authorization ID"""

    wait: int
    """Timeout in seconds (max 59)"""
