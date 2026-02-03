# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["WorkerCreateParams", "HTTP", "Mcp", "McpOauth2"]


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


class McpOauth2(TypedDict, total=False):
    authorization_url: str

    client_id: str

    client_secret: str

    external_id: str


class Mcp(TypedDict, total=False):
    retry: Required[int]

    timeout: Required[int]

    uri: Required[str]

    headers: Dict[str, str]

    oauth2: McpOauth2

    secrets: Dict[str, str]
