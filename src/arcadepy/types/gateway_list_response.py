# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GatewayListResponse", "ItemBinding", "ItemToolFilterDiscovery", "ItemToolFilter", "Item"]


class ItemBinding(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["static", "tenant", "project", "account"]] = None


class ItemToolFilterDiscovery(BaseModel):
    enabled: Optional[bool] = None


class ItemToolFilter(BaseModel):
    allowed_tools: Optional[List[str]] = None

    discovery: Optional[ItemToolFilterDiscovery] = None


class Item(BaseModel):
    allowed_passthrough_headers: Optional[List[str]] = None

    auth_type: Optional[str] = None

    binding: Optional[ItemBinding] = None

    consent_skip_client_ids: Optional[List[str]] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    id: Optional[str] = None

    instructions: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    status: Optional[str] = None

    tool_filter: Optional[ItemToolFilter] = None

    updated_at: Optional[str] = None

    user_source_id: Optional[str] = None


class GatewayListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
