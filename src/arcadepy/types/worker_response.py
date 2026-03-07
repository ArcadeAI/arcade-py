# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "WorkerResponse",
    "Binding",
    "HTTP",
    "HTTPSecret",
    "Mcp",
    "McpOauth2",
    "McpOauth2ClientSecret",
    "McpSecrets",
    "Requirements",
    "RequirementsAuthorization",
    "RequirementsAuthorizationOauth2",
]


class Binding(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["static", "tenant", "project", "account"]] = None


class HTTPSecret(BaseModel):
    binding: Optional[Literal["static", "tenant", "project", "account"]] = None

    editable: Optional[bool] = None

    exists: Optional[bool] = None

    hint: Optional[str] = None

    value: Optional[str] = None


class HTTP(BaseModel):
    retry: Optional[int] = None

    secret: Optional[HTTPSecret] = None

    timeout: Optional[int] = None

    uri: Optional[str] = None


class McpOauth2ClientSecret(BaseModel):
    binding: Optional[Literal["static", "tenant", "project", "account"]] = None

    editable: Optional[bool] = None

    exists: Optional[bool] = None

    hint: Optional[str] = None

    value: Optional[str] = None


class McpOauth2(BaseModel):
    authorization_url: Optional[str] = None

    client_id: Optional[str] = None

    client_secret: Optional[McpOauth2ClientSecret] = None

    redirect_uri: Optional[str] = None


class McpSecrets(BaseModel):
    binding: Optional[Literal["static", "tenant", "project", "account"]] = None

    editable: Optional[bool] = None

    exists: Optional[bool] = None

    hint: Optional[str] = None

    value: Optional[str] = None


class Mcp(BaseModel):
    headers: Optional[Dict[str, str]] = None

    oauth2: Optional[McpOauth2] = None

    retry: Optional[int] = None

    secrets: Optional[Dict[str, McpSecrets]] = None

    timeout: Optional[int] = None

    uri: Optional[str] = None


class RequirementsAuthorizationOauth2(BaseModel):
    met: Optional[bool] = None


class RequirementsAuthorization(BaseModel):
    met: Optional[bool] = None

    oauth2: Optional[RequirementsAuthorizationOauth2] = None


class Requirements(BaseModel):
    authorization: Optional[RequirementsAuthorization] = None

    met: Optional[bool] = None


class WorkerResponse(BaseModel):
    id: Optional[str] = None

    binding: Optional[Binding] = None

    enabled: Optional[bool] = None

    http: Optional[HTTP] = None

    managed: Optional[bool] = None

    mcp: Optional[Mcp] = None

    requirements: Optional[Requirements] = None

    type: Optional[Literal["http", "mcp", "unknown"]] = None
