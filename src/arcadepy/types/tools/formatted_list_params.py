# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FormattedListParams"]


class FormattedListParams(TypedDict, total=False):
    format: str
    """Provider format"""

    limit: int
    """Number of items to return (default: 25, max: 100)"""

    offset: int
    """Offset from the start of the list (default: 0)"""

    toolkit: str
    """Toolkit name"""
