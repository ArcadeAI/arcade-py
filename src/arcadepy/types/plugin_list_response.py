# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PluginListResponse",
    "ItemBinding",
    "ItemRateLimitConfigRule",
    "ItemRateLimitConfig",
    "ItemRetry",
    "ItemWebhookConfigAuthToken",
    "ItemWebhookConfigAuth",
    "ItemWebhookConfigEndpointsAccess",
    "ItemWebhookConfigEndpointsPost",
    "ItemWebhookConfigEndpointsPre",
    "ItemWebhookConfigEndpoints",
    "ItemWebhookConfig",
    "Item",
]


class ItemBinding(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["static", "tenant", "project", "account"]] = None


class ItemRateLimitConfigRule(BaseModel):
    allow_on_unavailable: Optional[bool] = None

    limit: Optional[int] = None

    match: Optional[str] = None

    time_unit: Optional[str] = None


class ItemRateLimitConfig(BaseModel):
    rules: Optional[List[ItemRateLimitConfigRule]] = None


class ItemRetry(BaseModel):
    backoff: Optional[str] = None

    base_delay_ms: Optional[int] = None

    enabled: Optional[bool] = None

    max_attempts: Optional[int] = None

    retry_on: Optional[List[str]] = None


class ItemWebhookConfigAuthToken(BaseModel):
    binding: Optional[Literal["static", "tenant", "project", "account"]] = None

    editable: Optional[bool] = None

    exists: Optional[bool] = None

    value: Optional[str] = None


class ItemWebhookConfigAuth(BaseModel):
    ca_cert: Optional[str] = None

    client_cert_configured: Optional[bool] = None

    client_key_configured: Optional[bool] = None

    token: Optional[ItemWebhookConfigAuthToken] = None

    type: Optional[str] = None


class ItemWebhookConfigEndpointsAccess(BaseModel):
    cache_enabled: Optional[bool] = None

    cache_ttl_ms: Optional[int] = None

    timeout_ms: Optional[int] = None

    url: Optional[str] = None


class ItemWebhookConfigEndpointsPost(BaseModel):
    cache_enabled: Optional[bool] = None

    cache_ttl_ms: Optional[int] = None

    timeout_ms: Optional[int] = None

    url: Optional[str] = None


class ItemWebhookConfigEndpointsPre(BaseModel):
    cache_enabled: Optional[bool] = None

    cache_ttl_ms: Optional[int] = None

    timeout_ms: Optional[int] = None

    url: Optional[str] = None


class ItemWebhookConfigEndpoints(BaseModel):
    access: Optional[ItemWebhookConfigEndpointsAccess] = None

    post: Optional[ItemWebhookConfigEndpointsPost] = None

    pre: Optional[ItemWebhookConfigEndpointsPre] = None


class ItemWebhookConfig(BaseModel):
    auth: Optional[ItemWebhookConfigAuth] = None

    endpoints: Optional[ItemWebhookConfigEndpoints] = None

    health_check_path: Optional[str] = None


class Item(BaseModel):
    binding: Optional[ItemBinding] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    health_status: Optional[str] = None

    id: Optional[str] = None

    name: Optional[str] = None

    plugin_type: Optional[str] = None

    rate_limit_config: Optional[ItemRateLimitConfig] = None

    retry: Optional[ItemRetry] = None

    status: Optional[Literal["inactive", "active"]] = None

    updated_at: Optional[str] = None

    updated_by: Optional[str] = None

    version: Optional[int] = None

    webhook_config: Optional[ItemWebhookConfig] = None


class PluginListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
