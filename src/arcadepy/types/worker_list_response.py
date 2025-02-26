# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .worker_response import WorkerResponse

__all__ = ["WorkerListResponse"]


class WorkerListResponse(BaseModel):
    items: Optional[List[WorkerResponse]] = None

    limit: Optional[int] = None

    offset: Optional[int] = None

    page_count: Optional[int] = None

    total_count: Optional[int] = None
