# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PluginCreateResponse",
    "Binding",
    "Hook",
    "RateLimitConfigRule",
    "RateLimitConfig",
    "Retry",
    "WebhookConfigAuthToken",
    "WebhookConfigAuth",
    "WebhookConfigEndpointsAccess",
    "WebhookConfigEndpointsPost",
    "WebhookConfigEndpointsPre",
    "WebhookConfigEndpoints",
    "WebhookConfig",
]


class Binding(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["static", "tenant", "project", "account"]] = None


class Hook(BaseModel):
    cache_enabled: Optional[bool] = None

    cache_ttl_ms: Optional[int] = None

    created_at: Optional[str] = None

    failure_mode: Optional[Literal["fail_closed", "fail_open"]] = None

    hook_point: Optional[str] = None

    id: Optional[str] = None

    name: Optional[str] = None

    phase: Optional[Literal["before", "after"]] = None

    plugin_id: Optional[str] = None

    priority: Optional[int] = None

    status: Optional[Literal["active", "inactive"]] = None

    timeout_ms: Optional[int] = None

    updated_at: Optional[str] = None

    version: Optional[int] = None


class RateLimitConfigRule(BaseModel):
    allow_on_unavailable: Optional[bool] = None

    limit: Optional[int] = None

    match: Optional[str] = None

    time_unit: Optional[str] = None


class RateLimitConfig(BaseModel):
    rules: Optional[List[RateLimitConfigRule]] = None


class Retry(BaseModel):
    backoff: Optional[str] = None

    base_delay_ms: Optional[int] = None

    enabled: Optional[bool] = None

    max_attempts: Optional[int] = None

    retry_on: Optional[List[str]] = None


class WebhookConfigAuthToken(BaseModel):
    binding: Optional[Literal["static", "tenant", "project", "account"]] = None

    editable: Optional[bool] = None

    exists: Optional[bool] = None

    value: Optional[str] = None


class WebhookConfigAuth(BaseModel):
    ca_cert: Optional[str] = None

    client_cert_configured: Optional[bool] = None

    client_key_configured: Optional[bool] = None

    token: Optional[WebhookConfigAuthToken] = None

    type: Optional[str] = None


class WebhookConfigEndpointsAccess(BaseModel):
    cache_enabled: Optional[bool] = None

    cache_ttl_ms: Optional[int] = None

    timeout_ms: Optional[int] = None

    url: Optional[str] = None


class WebhookConfigEndpointsPost(BaseModel):
    cache_enabled: Optional[bool] = None

    cache_ttl_ms: Optional[int] = None

    timeout_ms: Optional[int] = None

    url: Optional[str] = None


class WebhookConfigEndpointsPre(BaseModel):
    cache_enabled: Optional[bool] = None

    cache_ttl_ms: Optional[int] = None

    timeout_ms: Optional[int] = None

    url: Optional[str] = None


class WebhookConfigEndpoints(BaseModel):
    access: Optional[WebhookConfigEndpointsAccess] = None

    post: Optional[WebhookConfigEndpointsPost] = None

    pre: Optional[WebhookConfigEndpointsPre] = None


class WebhookConfig(BaseModel):
    auth: Optional[WebhookConfigAuth] = None

    endpoints: Optional[WebhookConfigEndpoints] = None

    health_check_path: Optional[str] = None


class PluginCreateResponse(BaseModel):
    binding: Optional[Binding] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    health_status: Optional[str] = None

    hooks: Optional[List[Hook]] = None

    id: Optional[str] = None

    name: Optional[str] = None

    plugin_type: Optional[str] = None

    rate_limit_config: Optional[RateLimitConfig] = None

    retry: Optional[Retry] = None

    status: Optional[Literal["inactive", "active"]] = None

    updated_at: Optional[str] = None

    updated_by: Optional[str] = None

    version: Optional[int] = None

    webhook_config: Optional[WebhookConfig] = None
