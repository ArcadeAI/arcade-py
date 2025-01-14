# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..tool_execution import ToolExecution

__all__ = ["ScheduledListResponse"]


class ScheduledListResponse(BaseModel):
    items: Optional[List[ToolExecution]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
