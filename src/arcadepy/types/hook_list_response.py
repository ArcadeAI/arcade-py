# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HookListResponse", "Item"]


class Item(BaseModel):
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


class HookListResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
