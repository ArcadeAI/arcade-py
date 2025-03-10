# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .tool_definition import ToolDefinition

__all__ = ["WorkerToolsResponse"]


class WorkerToolsResponse(BaseModel):
    items: Optional[List[ToolDefinition]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
