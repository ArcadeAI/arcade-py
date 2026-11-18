# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GatewayReplaceResponse", "Binding", "ToolFilterDiscovery", "ToolFilter"]


class Binding(BaseModel):
    id: Optional[str] = None

    type: Optional[Literal["static", "tenant", "project", "account"]] = None


class ToolFilterDiscovery(BaseModel):
    enabled: Optional[bool] = None


class ToolFilter(BaseModel):
    allowed_tools: Optional[List[str]] = None

    discovery: Optional[ToolFilterDiscovery] = None


class GatewayReplaceResponse(BaseModel):
    allowed_passthrough_headers: Optional[List[str]] = None

    auth_type: Optional[str] = None

    binding: Optional[Binding] = None

    consent_skip_client_ids: Optional[List[str]] = None

    created_at: Optional[str] = None

    description: Optional[str] = None

    id: Optional[str] = None

    instructions: Optional[str] = None

    name: Optional[str] = None

    slug: Optional[str] = None

    status: Optional[str] = None

    tool_filter: Optional[ToolFilter] = None

    updated_at: Optional[str] = None

    user_source_id: Optional[str] = None
