# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["WorkerUpdateParams", "HTTP", "Mcp", "McpOauth2"]


class WorkerUpdateParams(TypedDict, total=False):
    enabled: bool

    http: HTTP

    mcp: Mcp


class HTTP(TypedDict, total=False):
    retry: int

    secret: str

    timeout: int

    uri: str


class McpOauth2(TypedDict, total=False):
    authorization_url: str

    client_id: str

    client_secret: str


class Mcp(TypedDict, total=False):
    headers: Dict[str, str]

    oauth2: McpOauth2

    retry: int

    secrets: Dict[str, str]

    timeout: int

    uri: str
