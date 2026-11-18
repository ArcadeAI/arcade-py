# File generated from our OpenAPI spec. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ToolListExecutionsResponse", "Item"]


class Item(BaseModel):
    created_at: Optional[str] = None

    execution_status: Optional[str] = None

    execution_type: Optional[str] = None

    finished_at: Optional[str] = None

    id: Optional[str] = None

    run_at: Optional[str] = None

    started_at: Optional[str] = None

    tool_name: Optional[str] = None

    toolkit_name: Optional[str] = None

    toolkit_version: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None


class ToolListExecutionsResponse(BaseModel):
    items: Optional[List[Item]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
