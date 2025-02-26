# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkerCreateParams", "HTTP"]


class WorkerCreateParams(TypedDict, total=False):
    id: Required[str]

    enabled: Required[bool]

    http: HTTP


class HTTP(TypedDict, total=False):
    retry: Required[int]

    secret: Required[str]

    timeout: Required[int]

    uri: Required[str]
