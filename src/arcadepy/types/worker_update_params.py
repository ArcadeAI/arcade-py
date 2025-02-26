# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WorkerUpdateParams", "HTTP"]


class WorkerUpdateParams(TypedDict, total=False):
    enabled: bool

    http: HTTP


class HTTP(TypedDict, total=False):
    retry: int

    secret: str

    timeout: int

    uri: str
