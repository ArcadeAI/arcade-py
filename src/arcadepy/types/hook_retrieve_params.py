# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HookRetrieveParams"]


class HookRetrieveParams(TypedDict, total=False):
    binding_type: str
    """Filter by binding type (tenant or project)"""
