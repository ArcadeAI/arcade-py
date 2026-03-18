# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FormattedListParams"]


class FormattedListParams(TypedDict, total=False):
    filter: str
    """JSON metadata filter.

    Array fields (service_domains, operations): shorthand array or object with
    any_of/all_of/none_of operators (case-insensitive). Boolean fields: read_only,
    destructive, idempotent, open_world. Extras: case-sensitive key-value subset
    match.
    """

    format: str
    """Provider format"""

    include_all_versions: bool
    """Include all versions of each tool"""

    limit: int
    """Number of items to return (default: 25, max: 100)"""

    offset: int
    """Offset from the start of the list (default: 0)"""

    toolkit: str
    """Toolkit name"""

    user_id: str
    """User ID"""
