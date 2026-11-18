# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["HookBulkUpsertResponse", "Result"]


class Result(BaseModel):
    action: Optional[str] = None

    error: Optional[str] = None

    hook_id: Optional[str] = None

    hook_point: Optional[str] = None

    plugin_id: Optional[str] = None


class HookBulkUpsertResponse(BaseModel):
    failed: Optional[int] = None

    results: Optional[List[Result]] = None

    success: Optional[int] = None
