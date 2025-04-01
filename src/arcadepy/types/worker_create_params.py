# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorkerCreateParams", "HTTP", "Mcp"]


class WorkerCreateParams(TypedDict, total=False):
    id: Required[str]

    enabled: bool

    http: HTTP

    mcp: Mcp

    type: str


class HTTP(TypedDict, total=False):
    retry: Required[int]

    secret: Required[str]

    timeout: Required[int]

    uri: Required[str]


class Mcp(TypedDict, total=False):
    retry: Required[int]

    timeout: Required[int]

    uri: Required[str]
